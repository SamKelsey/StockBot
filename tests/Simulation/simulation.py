import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
conf_path = os.getcwd()
sys.path.append(conf_path)
print(conf_path)
from stockBot. import StockBot


# # some_file.py
# import sys
# # insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, 'root@7826009dda63:/workspaces/stockBot/Algorithms')

from simple import Simple

class Simulation:

    @staticmethod
    def startSimulation():
        print("starting sim...")

if __name__ == '__main__':
    Simulation.startSimulation()