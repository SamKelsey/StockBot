import abc 
from abc import ABC, abstractmethod

from pandas.core.series import Series

class DataSourceFactory:

    @staticmethod
    def getDataHandler(type):
        if (type == "LiveDataHandler"):
            return LiveDataSource()
        elif (type == "TestDataHandler"):
            return DataSource()

class DataSource(ABC): 

    @abstractmethod
    def get_data(self, ticker: str) -> Series:
        pass
    



class LiveDataSource(DataSource):
    def __init__(self):
        pass

    def get_data(self):
        pass