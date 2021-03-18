import abc 
from abc import ABC, abstractmethod

from config.config import getConfig
from stockBot.helpers.datahandler import DataHandler, DataHandlerFactory

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
        # if (currRow > preRow):
        #     return "Buy"
        # elif (currRow < preRow):
        #     return "Sell"
        # else:
        #     return "Nothing"
        
        # print("Running: Simple Algorithm")