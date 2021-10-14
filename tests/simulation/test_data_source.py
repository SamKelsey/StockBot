import os
import logging
from stockBot.helpers.data_source import DataSource
from typing import Dict, Iterable, List, Tuple
from pandas import read_csv
from pandas.core.frame import DataFrame
from pandas.core.series import Series

logger = logging.getLogger()

class FinishedTestDataException(StopIteration):

    def __init__(self, ticker: str):
        self.ticker = ticker
        super().__init__()

"""
A class to simulate a DataSource, that returns up-to-date financial data on stocks.
Successively call the get_data() method to retrieve a new row of data from your datasources.
Catch a 'StopIteration' error for when the test data is finished.
"""
class TestDataSource(DataSource):

    test_data_files_loc: str                    # Test data directory from root
    test_data_file_names: List[str]             # List of tickers in the test data.
    test_data: Dict                             # Dictionary of iterable test data df's

    def __init__(self, test_data_files_loc="tests/test_data"):
        self.test_data_file_names = self._read_test_data_files(test_data_files_loc)
        self.test_data = {}
        for file in self.test_data_file_names:
            self.test_data[file[:-4]] = TestDataSource._read_df_to_iterable(test_data_files_loc, file)


    """ 
    @desc       Get a row of data from test data. 
    @args       - ticker: A string that uniquely identifies a stock.
    @throws     - StopIteration: Error to indicate the test data is finished.
    @returns    - A row (Pandas Series) of data.
    """
    def get_data(self, ticker: str) -> Series:
        try:
            return next(self.test_data[ticker])[1]
        except StopIteration:
            raise FinishedTestDataException(ticker)


    """ 
    @desc       Read a list of all test data files to be used in simulation.
    @args       - path: Path to data files directory.
    @returns    - A list of data files.
    """
    def _read_test_data_files(self, path) -> List[str]:
        return [file for file in os.listdir(path) if file[-4:] == ".csv"]


    """ 
    @desc       Returns an iterable object from a csv file.
    @args       - base_path: Root path of file as a string.
                - file_name: Name of file as a string.
    @returns    - Iterable object of the file.
    """
    @staticmethod
    def _read_df_to_iterable(base_path: str, file_name: str) -> Iterable:
        return read_csv(f"{base_path}/{file_name}").iterrows()



if __name__ == "__main__":
    data_source = TestDataSource()
    while True:

        try:
            data_source.get_data("AAPL")
        except FinishedTestDataException as e:
            logger.error(e.ticker)
            break