import os
import sys
import logging
from tests.simulation.test_data_source import TestDataSource, FinishedTestDataException
from tests.simulation.test_broker import TestBroker
from stockBot.helpers.algorithms import AlgorithmFactory
from stockBot.helpers.brokers import BrokerException

data_source = TestDataSource()
broker = TestBroker(100_000)


def main():
    argv = sys.argv[1:]
    if len(argv) == 0:
        argv = ["ExampleAlgo", "tests/test_data"]

    algo = AlgorithmFactory.getAlgorithm(argv[0], broker, data_source)

    try:
        algo.start("AAPL")
    except FinishedTestDataException as e:
        logger.info(f"Test finished for {e.ticker}. Final balance: {broker.get_total_equity()}")


if __name__ == '__main__':
    os.environ['PYTHON_ENV'] = "test"
    
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    main()  
  
