import abc 
from abc import ABC, abstractmethod

import pandas as pd
from pandas_datareader import data

from collections import defaultdict

import requests
from bs4 import BeautifulSoup

from datetime import datetime, timedelta

from config.config import getConfig
from stockBot.helpers.dataHandler import DataHandler, DataHandlerFactory
from stockBot.helpers.brokerFactory import BrokerFactory
from stockBot.helpers.symbolInfo import SymbolInfo

class Algorithm(ABC): 

    @abstractmethod
    def run(self):
        pass


class AlgorithmFactory:

    @staticmethod
    def getAlgorithm(type):
        if (type == "YAHSCRAPER"):
            return YahScraper()
        elif (type == "SIMPLE"):
            return Simple()


class Simple(Algorithm):
      
    def run(self):

        dataConfig = getConfig().get("DataHandler", "DataClass")
        data = DataHandlerFactory.getDataHandler(dataConfig)

        currRow, prevRow = data.getData()

        currRow = currRow['50dayEWM']
        prevRow = prevRow['50dayEWM']

        if (currRow > prevRow):
            return "Buy"
        elif (currRow < prevRow):
            return "Sell"
        else:
            return "Nothing"

class YahScraper(Algorithm):
    # Number of days to calculate change over.
    period = 3
    if (period < 3):
        raise ValueError("period must be greater than 2")

    def run(self):
        # tickerInfo = YahScraper.getTickers()
        tickerInfo = [
            {
                "symbol": "AAPL"
            },
            {
                "symbol": "SBUX"
            }
        ]

        data = YahScraper.getTickersData(tickerInfo)
        self.tickerInfo = YahScraper.analyseTickers(data, tickerInfo)
        print(self.tickerInfo)

        broker = BrokerFactory.getBroker()
        broker.buy()

    @staticmethod
    def getTickers():
        tickerInfo = defaultdict(dict)
        url = "https://finance.yahoo.com/most-active/"

        res = requests.get(url)
        soup = BeautifulSoup(res.content, "lxml")
        for item in soup.select('.simpTblRow'):
            symbol = item.select('[aria-label=Symbol]')[0].get_text()
            tickerInfo[symbol] = {}
        return tickerInfo

    @staticmethod
    def getTickersData(tickerInfo):
        end_date = datetime.today().strftime('%Y-%m-%d')
        start_date = datetime.today() - timedelta(days=YahScraper.period)
        start_date = start_date.strftime('%Y-%m-%d')

        tickers = list(tickerInfo.keys())
        return data.DataReader(tickers, 'yahoo', start_date, end_date)
    
    @staticmethod
    def analyseTickers(data, tickerInfo):
        currPrices = data.iloc[-1]['Adj Close']
        prevPrices = data.iloc[0]['Adj Close']
        for ticker in tickerInfo:
            change = ((prevPrices[ticker] - currPrices[ticker])/prevPrices[ticker])*100

            tickerInfo[ticker]["change"] = change
            
            if (change > 0):
                tickerInfo[ticker]["result"] = "BUY"
            elif (change < 0):
                tickerInfo[ticker]["result"] = "SELL"
            else:
                tickerInfo[ticker]["result"] = "NONE"

        return tickerInfo
