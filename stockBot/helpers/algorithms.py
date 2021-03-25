import abc 
from abc import ABC, abstractmethod
import sys
print(sys.path)

import requests
from bs4 import BeautifulSoup

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
    def __init__(self):
        self.URL = "https://finance.yahoo.com/most-active/"
        self.tickers = []
        pass

    def run(self):
        tickers = self.getTickers()

    def getTickers(self):
        res = requests.get(self.URL)
        soup = BeautifulSoup(res.content, "lxml")
        for item in soup.select('.simpTblRow'):
            # print(item.select('[aria-label=Symbol]')[0].get_text())
            # print(item.select('[aria-label=Name]')[0].get_text())
            # print(item.select('[aria-label*=Price]')[0].get_text())
            # print(item.select('[aria-label=Change]')[0].get_text())
            # print(item.select('[aria-label="% change"]')[0].get_text())
            # print(item.select('[aria-label="Market cap"]')[0].get_text())
            # print(item.select('[aria-label*="Avg vol (3-month)"]')[0].get_text())
            # print(item.select('[aria-label*="PE ratio (TTM)"]')[0].get_text())
            # print('____________________________')
            self.tickers.append(item.select('[aria-label=Symbol]')[0].get_text())

