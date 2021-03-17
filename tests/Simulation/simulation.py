import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

from configparser import ConfigParser as CP

from stockBot.helpers.algorithms import AlgorithmFactory
from stockBot.helpers.configHandler import ConfigHandler

import pandas as pd

class Simulation:

    def __init__(self):
        configParser = CP()   
        configFilePath = 'tests/simulation/config.ini'
        configParser.read(configFilePath)
        self.config = configParser


    def startSimulation(self):
        print("Running: Simulation")
        dataHandlerType = self.config.get("DataHandler", "DataClass")
        algorithm = AlgorithmFactory.getAlgorithm("SIMPLE", dataHandlerType)
        df = self.getDataFrame("AAPL")
        

        for i in range(len(df)-1):
            i+=1
            row = df.iloc[i]
            prevRow = df.iloc[i-1]
            res = algorithm.run()
            #print(res)

    def getDataFrame(self, ticker):
        path = os.path.join("tests/test_data", f"{ticker}.csv")
        df = pd.read_csv(path)
        return df



if __name__ == '__main__':
    sim = Simulation()
    sim.startSimulation()
