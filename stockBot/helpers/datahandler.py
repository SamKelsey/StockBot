import abc 
from abc import ABC, abstractmethod

class DataHandlerFactory:
    @staticmethod
    def getDataHandler(type):
        print(type)
        if (type == "LiveDataHandler"):
            return LiveDataHandler()
        elif (type == "TestDataHandler"):
            return TestDataHandler()

class DataHandler(ABC): 

    @abstractmethod
    def run(self):
        pass


class LiveDataHandler(DataHandler):
    def __init__(self):
        print("CREATED: DataHandler")

    def run(self):
        print("RUNNING")


class TestDataHandler(DataHandler):
    def __init__(self):
        print("CREATED: TestDataHandler")

    def run(self):
        print("RUNNING")