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

        while True:
            try:
                print(algorithm.run())
            except IndexError:
                print("Finished")
                break




if __name__ == '__main__':
    sim = Simulation()
    sim.startSimulation()
  
    
