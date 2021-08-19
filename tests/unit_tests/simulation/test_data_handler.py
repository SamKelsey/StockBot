from typing import List, Tuple
import unittest
import numpy as np
import pandas as pd
from unittest.mock import MagicMock, patch

from pandas.core.frame import DataFrame
from tests.simulation.data_handler import DataHandler, StatusFlag

class TestDataHandler(unittest.TestCase):

    @patch("tests.simulation.data_handler.os")
    def test_read_data_files(self, mock_os):
        test_files, expected_result = self.get_data_files()
        mock_os.listdir.return_value = test_files

        data_handler = DataHandler()
        actual_result = data_handler._read_test_data_files("")
        self.assertEqual(expected_result, actual_result)

    def test_data_is_finished(self):
        data_handler = DataHandler()
        data_handler._test_data_files = self.get_data_files()[1]

        result1 = data_handler._data_is_finished(2)
        result2 = data_handler._data_is_finished(1)

        self.assertEqual(True, result1)
        self.assertEqual(False, result2)

    @patch("tests.simulation.data_handler.DataHandler._data_is_finished")
    def test_when_data_finished_flag_set(self, mock_data_is_finished):
        mock_data_is_finished.return_value = True

        data_handler = DataHandler()
        data_handler._read_df(1)

        self.assertEqual(
            StatusFlag.FINISHED,
            data_handler.status_flag
        )

    def test_when_curr_df_is_none_read_df(self):
        data_handler = DataHandler()
        data_handler._read_df = MagicMock(return_value=self.get_example_df(4, 4))
        data_handler._curr_df = None
        data_handler.get_data()
        data_handler._read_df.assert_called_once()

    def test_when_data_file_is_finished(self):
        data_handler = DataHandler()
        prev_curr_file = data_handler._curr_file
        data_handler._curr_df = self.get_example_df(4, 4)

        new_df = self.get_example_df(4, 4)
        data_handler._read_df = MagicMock(return_value=new_df)
        data_handler._index = new_df.shape[0]
        data_handler.get_data()

        self.assertEqual(prev_curr_file+1, data_handler._curr_file)
        self.assertEqual(data_handler._init_index+1, data_handler._index)
        self.assertTrue(new_df.equals(data_handler._curr_df))

    """
    Returns example directory of files and expected filtered result.
    """
    def get_data_files(self) -> Tuple[List[str], List[str]]:
        return (
            ["AAPL.csv", "T_X.csv", "examplE.csv", "Examp.csvle", "anothercsv"],
            ["AAPL.csv", "T_X.csv", "examplE.csv"]
        )

    """
    @desc       Get a sample dataframe of ints and a specified size
    @args       - rows: Number of rows in returned dataframe
                - cols: Number of colums in returned dataframe
    @returns    - Randomly generated Pandas Dataframe of ints.
    """
    def get_example_df(self, rows: int, cols: int) -> DataFrame:
        np_array = np.random.randint(4, size=(rows, cols))
        return pd.DataFrame(np_array)

if __name__ == "__main__":
    unittest.main()