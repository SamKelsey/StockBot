import sys
import os
sys.path.append(os.getcwd())

from tests.simulation.data_handler import DataHandler
import logging

class Simulation: 

    def __init__(self):
        os.environ['PYTHON_ENV'] = "test"


    def run(self):
        logger.info('Running simulation.')
        data_handler = DataHandler()
        while True:
            data_row, flag = data_handler.get_data()
            if (flag == 1):
                logger.info("Simulation complete.")
                break



if __name__ == '__main__':
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    sim = Simulation()
    sim.run()
  
    
