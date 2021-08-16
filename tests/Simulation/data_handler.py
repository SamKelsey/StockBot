import sys
import os
sys.path.append(os.getcwd())

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
    
    __curr_file: int                            # Index of current data file
    __curr_df: DataFrame                        # Dataframe for current data file
    __index: int                                # Index location in current dataframe
    __test_data_files: List[str]                # List of data files for simulation
    __test_data_files_loc = "tests/test_data/"  # Test data directory
    __init_index = 0                            # Initial index for sampling test data
    __finished_flag_status = 1                  # Flag value for finished the test data
    __running_flag_status = 0                   # Flag value for not finished the test data


    def __init__(self):
        self.__curr_file = 0
        self.status_flag = self.__running_flag_status
        self.__index = self.__init_index
        self.__test_data_files = self.__get_test_data_files()
        self.__curr_df = self.__read_df()

    """ Get a list of all test data files to be used in simulation. """
    def __get_test_data_files(self) -> List[str]:
        return [file for file in os.listdir(self.__test_data_files_loc) if file[-4:] == ".csv"]

    """ Read new df to curr_df and reset index counter. """
    def __read_df(self) -> DataFrame:
        if (self.__curr_file >= len(self.__test_data_files)-1):
            self.status_flag = self.__finished_flag_status
        logger.info(f"Using {self.__test_data_files[self.__curr_file][:-4]} test data set.")
        file = self.__test_data_files[self.__curr_file]
        df = read_csv(f"{self.__test_data_files_loc}/{file}")
        self.__index = self.__init_index
        return df
        
    """ 
    Get a row of data from test data and increment index counter. 
    @returns    - A row (Pandas Series) of data.
                - The status flag
    """
    def get_data(self) -> Tuple[Series, int]:
        if (self.__index >= self.__curr_df.shape[0]):
            self.__curr_file += 1
            self.__curr_df = self.__read_df()
        row = self.__curr_df.iloc[self.__index]
        self.__index += 1
        return row, self.status_flag


if __name__ == "__main__":
    data_handler = DataHandler()
    data_handler.get_data()