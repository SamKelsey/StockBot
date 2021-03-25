import os 
import sys 
conf_path = os.getcwd()
sys.path.append(conf_path)

print(sys.path)

from stockBot.helpers.algorithms import AlgorithmFactory, Simple

class StockBot:

    @staticmethod
    def startBot():
        print("Starting: Stockbot")
        algorithm = AlgorithmFactory.getAlgorithm("SIMPLE")
        algorithm.run()

    def getStatus(self):
        return "Running: Stockbot"

if __name__ == '__main__':
    StockBot.startBot()