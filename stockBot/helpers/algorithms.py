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

class Algorithm(ABC): 

    @abstractmethod
    def run(self):
        pass


class AlgorithmFactory:

    @staticmethod
    def getAlgorithm(type):
        if (type == "SIMPLE"):
            return Simple()


class Simple(Algorithm):
    
    def __init__(self):
        pass
        # print("Created: Simple Algorithm")
    
    def run(self):

        dataHandler = getConfig().get("DataHandler", "DataClass")
        data = DataHandlerFactory.getDataHandler(dataHandler)

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
    period = 2


    def __init__(self):
        self.URL = "https://finance.yahoo.com/most-active/"
        self.tickers = []
        pass

    def run(self):
        self.tickerInfo = defaultdict(dict)
        
        self.getTickers()
        # self.tickerInfo = {
        #     'AAPL':{},
        #     'SBUX':{}
        # }

        self.getTickersData()
        self.analyseTickers()


    def getTickers(self):
        res = requests.get(self.URL)
        soup = BeautifulSoup(res.content, "lxml")
        for item in soup.select('.simpTblRow'):
            symbol = item.select('[aria-label=Symbol]')[0].get_text()
            self.tickerInfo[symbol] = {}

    def getTickersData(self):
        end_date = datetime.today().strftime('%Y-%m-%d')
        start_date = datetime.today() - timedelta(days=YahScraper.period)
        start_date = start_date.strftime('%Y-%m-%d')

        tickers = list(self.tickerInfo.keys())
        self.panel_data = data.DataReader(tickers, 'yahoo', start_date, end_date)
    
    def analyseTickers(self):
        currPrices = self.panel_data.iloc[-1]['Adj Close']
        prevPrices = self.panel_data.iloc[0]['Adj Close']
        for ticker in self.tickerInfo:
            change = ((prevPrices[ticker] - currPrices[ticker])/prevPrices[ticker])*100

            self.tickerInfo[ticker]["change"] = change
            
            if (change > 0):
                self.tickerInfo[ticker]["result"] = "BUY"
            elif (change < 0):
                self.tickerInfo[ticker]["result"] = "SELL"
            else:
                self.tickerInfo[ticker]["result"] = "NONE"

        print(self.tickerInfo)
