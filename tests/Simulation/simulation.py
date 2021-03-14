import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.helpers.algorithms import AlgorithmFactory

class Simulation:

    @staticmethod
    def startSimulation():
        print("Running: Simulation")
        algorithm = AlgorithmFactory.getAlgorithm("SIMPLE")
        print(algorithm)

if __name__ == '__main__':
    Simulation.startSimulation()