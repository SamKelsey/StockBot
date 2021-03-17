import os 
import sys 
conf_path = os.getcwd()
sys.path.append(conf_path)

import configparser

from stockBot.helpers.algorithms import Simple

class StockBot:

    @staticmethod
    def startBot():
        configParser = configparser.ConfigParser()   
        configFilePath = 'stockbot/config.ini'
        return "Starting: Stockbot"

    def getStatus(self):
        return "Running: Stockbot"

if __name__ == '__main__':
    StockBot.startBot()