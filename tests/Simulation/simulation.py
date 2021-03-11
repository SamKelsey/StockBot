import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.Alogrithms.simple import Simple

class Simulation:

    @staticmethod
    def startSimulation():
        print("starting sim...")

if __name__ == '__main__':
    Simulation.startSimulation()