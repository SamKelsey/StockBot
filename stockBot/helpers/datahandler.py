import abc 
from abc import ABC, abstractmethod

class DataHandlerFactory:

    @staticmethod
    def getDataHandler(type):
        if (type == "LiveDataHandler"):
            return LiveDataHandler()
        elif (type == "TestDataHandler"):
            from tests.simulation.testDataHandler import TestDataHandler
            return TestDataHandler()

class DataHandler(ABC): 

    @abstractmethod
    def getData(self):
        pass



class LiveDataHandler(DataHandler):
    def __init__(self):
        pass
    # print("CREATED: DataHandler")

    def getData(self):
        pass