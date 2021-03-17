import abc 
from abc import ABC, abstractmethod

from stockBot.helpers.datahandler import DataHandler, DataHandlerFactory

class Algorithm(ABC): 

    @abstractmethod
    def run(self):
        pass


class AlgorithmFactory:

    @staticmethod
    def getAlgorithm(type, dataHandlerType):
        if (type == "SIMPLE"):
            return Simple(dataHandlerType)


class Simple(Algorithm):
    
    def __init__(self, dataHandlerType):
        self.dataHandler = dataHandlerType
        print("Created: Simple Algorithm")
    
    def run(self):

        data = DataHandlerFactory.getDataHandler(self.dataHandler)
        print(data)
        # if (currRow > preRow):
        #     return "Buy"
        # elif (currRow < preRow):
        #     return "Sell"
        # else:
        #     return "Nothing"
        
        print("Running: Simple Algorithm")