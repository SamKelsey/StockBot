import os
from stockBot.helpers.algorithms import AlgorithmFactory, Simple, YahScraper

class StockBot:

    @staticmethod
    def startBot():
        print("Starting: Stockbot")
        algorithm = AlgorithmFactory.getAlgorithm("SIMPLE")
        algorithm.start()

    def getStatus(self):
        return "Running: Stockbot"

if __name__ == '__main__':
    # set env variable.
    os.environ['PYTHON_ENV'] = "dev"

    algo = AlgorithmFactory.getAlgorithm("YAHSCRAPER")
    algo.start()