import os
import sys
import logging
from tests.simulation.data_handler import DataHandler, StatusFlag
from tests.simulation.bank_account import BankAccount
from stockBot.helpers.algorithms import Algorithm, AlgorithmFactory

""" 
A class responsible for running a simulation and returning the results in terms of money gained/lost. 
"""
class Simulation: 

    def __init__(self):
        pass

    """
    @desc       Kick-off simulation and return results when finished
    @args       - data_loc: Path to test data directory for simulation to use.
                - algo: Algorithm for the simulation to use.
    @returns    - (Float) Value of money gained/lost over all datasets in the simulation.
    """
    def run(self, data_loc: str, algo: Algorithm):
        """
        - Initialize bank acc
        - Initialize data handler
        - Read first row of data
        - Enter while loop
            - Read row of data
            - Buy/sell/nothing using algorithm?
            - Perform transaction on bank acc
        """
        bank_account = BankAccount()
        data_handler = DataHandler(data_loc)
        flag = ""

        while flag != StatusFlag.FINISHED:
            row = data_handler.get_data()
            transaction = algo.run(row)

            receipt = bank_account.perform(transaction)


def main(argv=["ExampleAlgo", "tests/test_data"]):
    sim = Simulation()
    algo = AlgorithmFactory.getAlgorithm(argv[0])
    sim.run(algo, argv[1])


if __name__ == '__main__':
    os.environ['PYTHON_ENV'] = "test"
    argv = sys.argv[1:]
    
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    main(argv)  
  
    
