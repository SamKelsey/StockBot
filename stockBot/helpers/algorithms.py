import abc 
from abc import ABC, abstractmethod
import sys
print(sys.path)
# import requests
# from bs4 import BeautifulSoup

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
        self.URL = "https://in.finance.yahoo.com/most-active"
        pass

    def getHtml(self):
        res = requests.get(self.URL)
        print(res)
