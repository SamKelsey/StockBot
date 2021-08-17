import sys
import os
sys.path.append(os.getcwd())

from pandas import DataFrame

import unittest
from unittest.mock import patch
from tests.simulation.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):

    @patch("tests.simulation.data_handler.DataHandler._read_df")
    @patch("tests.simulation.data_handler.os")
    def test_get_data_files(self, mock_os, mock_read_df):
        test_files = ["AAPL.csv", "T_X.csv", "ANOTHERcsv"]
        mock_os.listdir.return_value = test_files
        mock_read_df.return_value = {}

        data_handler = DataHandler()

        expected_result = ["AAPL.csv", "T_X.csv"]
        self.assertEqual(expected_result, data_handler._test_data_files)


    # TODO - This needs changed, too broad a test.
    # @patch("tests.simulation.data_handler.os")
    # @patch("tests.simulation.data_handler.read_csv")
    # def test_get_data(self, mock_pandas_read_csv, mock_os):
    #     mock_os.listdir.return_value = [
    #         "test.csv",
    #         "another_test.csv"
    #     ]
    #     mock_pandas_read_csv.return_value = DataFrame.from_dict({
    #         "date": [1, 2, 3, 4],
    #         "name": ["sam", "jess", "craig", "aaron"]
    #     })

    #     data_handler = DataHandler()
    #     self.assertEqual(["test.csv", "another_test.csv"], data_handler._DataHandler__test_data_files)


if __name__ == "__main__":
    unittest.main()