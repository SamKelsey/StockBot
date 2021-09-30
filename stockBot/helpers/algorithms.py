import abc 
from abc import ABC, abstractmethod

import pandas as pd
from pandas_datareader import data

from collections import defaultdict

import requests
from bs4 import BeautifulSoup

from datetime import datetime, timedelta

from config.config import getConfig
from stockBot.helpers.data_source import DataSource, DataSourceFactory
from stockBot.helpers.brokers import BrokerFactory, Broker
from stockBot.helpers.transaction import Transaction, Action

class Algorithm(ABC): 

    def __init__(self, broker: Broker, data_source: DataSource):
        self.broker = broker
        self.data_source = data_source

    """
    @desc       Kicks off an algorithm, against a given stock, which runs indefinitely.
    @args       - stock_ticker: A string that identifies a stock.
    @returns    - Nothing
    """
    @abstractmethod
    def start(self, stock_ticker: str) -> None:
        pass


class AlgorithmFactory:

    @staticmethod
    def getAlgorithm(type, broker: Broker, data_source: DataSource):
        if (type == "YAHSCRAPER"):
            return YahScraper(broker, data_source)
        elif (type == "SIMPLE"):
            return Simple(broker, data_source)
        elif (type == "ExampleAlgo"):
            return ExampleAlgo(broker, data_source)



class ExampleAlgo(Algorithm):
    def start(self, ticker):
        data = self.data_source.get_data(ticker)
        transaction = Transaction(
            Action.BUY,
            100,
            30.00
        )
        receipt = self.broker.place_order(transaction)
        print(receipt.curr_balance)
        
        


class Simple(Algorithm):
      
    def start(self):

        dataConfig = getConfig().get("DataHandler", "DataClass")
        data = DataSourceFactory.getDataHandler(dataConfig)

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

    def start(self):
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
