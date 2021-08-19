import os
import logging
from typing import List, Tuple
from pandas import read_csv
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from enum import Enum

logger = logging.getLogger()

""" 
Flag to show if datasets are finished and no more data is available. 
"""
class StatusFlag(Enum):
    NOT_FINISHED = 0
    FINISHED = 1

"""
A class to simulate calls to an api that returns up-to-date financial data on stocks.
Successively call the get_data() method to retrieve a new row of data from your datasources.
"""
class DataHandler():

    status_flag: StatusFlag                    # Flag to show if at end of data
    test_data_files_loc: str                   # Test data directory from root
    
    _curr_file: int                            # Index of current data file
    _curr_df: DataFrame                        # Dataframe for current data file
    _index: int                                # Index location in current dataframe
    _test_data_files: List[str]                # List of data files for simulation
    _init_index = 0                            # Initial index for sampling test data


    def __init__(self, test_data_files_loc="tests/test_data"):
        self._curr_file = 0
        self.status_flag = StatusFlag.NOT_FINISHED
        self._index = self._init_index
        self.test_data_files_loc = test_data_files_loc
        self._test_data_files = self._read_test_data_files(test_data_files_loc)

    """ 
    @desc       Get a row of data from test data. 
    @args       -
    @returns    - A row (Pandas Series) of data.
                - A status flag
    """
    def get_data(self) -> Tuple[Series, int]:

        if (self._curr_df is None):
            self._curr_df = self._read_df(self._curr_file)

        if (self._index >= self._curr_df.shape[0]):
            self._curr_file += 1
            self._index = self._init_index
            self._curr_df = self._read_df(self._curr_file)

        row = self._curr_df.iloc[self._index]
        self._index += 1
        return row, self.status_flag

    """ 
    @desc       Read a list of all test data files to be used in simulation.
    @args       - path: Path to data files directory.
    @returns    - A list of data files.
    """
    def _read_test_data_files(self, path) -> List[str]:
        return [file for file in os.listdir(path) if file[-4:] == ".csv"]

    """ 
    @desc       Returns a new df.
    @args       - i: Index position of file.
    @returns    - Dataframe of file
    """
    def _read_df(self, i: int) -> DataFrame:
        if (self._data_is_finished(i)):
            self.status_flag = StatusFlag.FINISHED
            return
        file = self._test_data_files[i]
        return read_csv(f"{self.test_data_files_loc}/{file}")

    """ 
    @desc       Is the data finished
    @args       - Index position of file.
    @returns    - boolean
    """
    def _data_is_finished(self, i: int):
        if (i >= len(self._test_data_files)-1):
            return True
        return False


if __name__ == "__main__":
    data_handler = DataHandler()

    print(data_handler.get_data())