import os 
import sys 
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.algorithms_package.algorithms import Simple

class StockBot:

    @staticmethod
    def startBot():
        return "Starting: Stockbot"

    def getStatus(self):
        return "Running: Stockbot"

if __name__ == '__main__':
    StockBot.startBot()