from stockBot.helpers.dataHandler import DataHandler
from tests.simulation.simulation import Simulation

import pandas as pd
import os


class TestDataHandler(DataHandler):
    DF = ""
    INDEX = 0

    def getData(self):
        TestDataHandler.INDEX += 1
        i = TestDataHandler.INDEX
        if (i == 1):
            TestDataHandler.getDataFrame("AAPL")
        row = TestDataHandler.DF.iloc[i]
        prevRow = TestDataHandler.DF.iloc[i-1]
        return row, prevRow

    @classmethod
    def getDataFrame(self, ticker):
        path = os.path.join("tests/test_data", f"{ticker}.csv")
        df = pd.read_csv(path)
        TestDataHandler.DF = df
