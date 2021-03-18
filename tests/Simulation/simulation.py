import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.helpers.algorithms import AlgorithmFactory
from config.config import getConfig

import pandas as pd

class Simulation:

    def __init__(self):
        os.environ['PYTHON_ENV'] = "test"


    def startSimulation(self):
        print("Running: Simulation")
        algorithm = AlgorithmFactory.getAlgorithm("SIMPLE")
        df = self.getDataFrame("AAPL")
        
        algorithm.run()
        # for i in range(len(df)-1):
        #     i+=1
        #     row = df.iloc[i]
        #     prevRow = df.iloc[i-1]
        #     res = algorithm.run()

    def getDataFrame(self, ticker):
        path = os.path.join("tests/test_data", f"{ticker}.csv")
        df = pd.read_csv(path)
        return df



if __name__ == '__main__':
    sim = Simulation()
    sim.startSimulation()
    
