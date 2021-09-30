import os
import sys
import logging
from tests.simulation.test_data_source import TestDataSource
from tests.simulation.test_broker import TestBroker
from stockBot.helpers.algorithms import AlgorithmFactory

data_source = TestDataSource()
broker = TestBroker(100_000)


def main():
    argv = sys.argv[1:]
    if len(argv) == 0:
        argv = ["ExampleAlgo", "tests/test_data"]

    algo = AlgorithmFactory.getAlgorithm(argv[0], broker, data_source)
    # Run simulation in try-catch block and catch out-of-data errors then display final balance.
    algo.start("any string")

if __name__ == '__main__':
    os.environ['PYTHON_ENV'] = "test"
    
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    main()  
  
