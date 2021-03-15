import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.helpers.algorithms import AlgorithmFactory

import pandas as pd

class Simulation:


    def getDataFrame(self, ticker):
        path = os.path.join("tests/test_data", f"{ticker}.csv")
        df = pd.read_csv(path)
        return df

    def startSimulation(self):
        print("Running: Simulation")
        algorithm = AlgorithmFactory.getAlgorithm("SIMPLE")
        df = self.getDataFrame("AAPL")
        # df  = df.tail()

        for i in range(len(df)-1):
            i+=1
            row = df.iloc[i]
            prevRow = df.iloc[i-1]
            res = algorithm.run(row['50dayEWM'], prevRow['50dayEWM'])
            print(res)



if __name__ == '__main__':
    sim = Simulation()
    sim.startSimulation()