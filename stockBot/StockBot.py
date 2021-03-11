import os 
import sys 
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.algorithms.Simple import Simple

class StockBot:

    @staticmethod
    def startBot():
        print("starting bot")

    def getStatus(self):
        return "running stockBot..."

if __name__ == '__main__':
    StockBot.startBot()