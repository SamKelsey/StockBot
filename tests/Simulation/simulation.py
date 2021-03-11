import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.algorithms.AlgorithmFactory import AlgorithmFactory

class Simulation:

    @staticmethod
    def startSimulation():
        print("starting sim...")
        algorithmFactory = AlgorithmFactory()
        algorithm = algorithmFactory.getAlgorithm("SIMPLE")
        print(algorithm)

if __name__ == '__main__':
    Simulation.startSimulation()