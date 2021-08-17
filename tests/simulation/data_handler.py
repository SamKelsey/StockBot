import os
import logging
from typing import List, Tuple
from pandas import read_csv
from pandas.core.frame import DataFrame
from pandas.core.series import Series

logger = logging.getLogger()

"""
A class responsible for delivering the test data in single, incrementing rows.
"""
class DataHandler():

    """ 
    Flag to describe if at the end of the test data
    0 => Not finished
    1 => Finished
    """
    status_flag: int
    
    _curr_file: int                            # Index of current data file
    _curr_df: DataFrame                        # Dataframe for current data file
    _index: int                                # Index location in current dataframe
    _test_data_files: List[str]                # List of data files for simulation
    _test_data_files_loc = "tests/test_data/"  # Test data directory
    _init_index = 0                            # Initial index for sampling test data
    _finished_flag_status = 1                  # Flag value for finished the test data
    _running_flag_status = 0                   # Flag value for not finished the test data


    def __init__(self):
        self._curr_file = 0
        self.status_flag = self._running_flag_status
        self._index = self._init_index
        self._test_data_files = self._get_test_data_files()
        self._curr_df = self._read_df()

    """ Get a list of all test data files to be used in simulation. """
    def _get_test_data_files(self) -> List[str]:
        return [file for file in os.listdir(self._test_data_files_loc) if file[-4:] == ".csv"]

    """ Read new df to curr_df and reset index counter. """
    def _read_df(self) -> DataFrame:
        if (self._curr_file >= len(self._test_data_files)-1):
            self.status_flag = self._finished_flag_status
        logger.info(f"Using {self._test_data_files[self._curr_file][:-4]} test data set.")
        file = self._test_data_files[self._curr_file]
        df = read_csv(f"{self._test_data_files_loc}/{file}")
        self._index = self._init_index
        return df
        
    """ 
    Get a row of data from test data and increment index counter. 
    @returns    - A row (Pandas Series) of data.
                - The status flag
    """
    def get_data(self) -> Tuple[Series, int]:
        if (self._index >= self._curr_df.shape[0]):
            self._curr_file += 1
            self._curr_df = self._read_df()
        row = self._curr_df.iloc[self._index]
        self._index += 1
        return row, self.status_flag


if __name__ == "__main__":
    data_handler = DataHandler()
    data_handler.get_data()