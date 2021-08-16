import sys
import os
sys.path.append(os.getcwd())

from pandas import DataFrame

import unittest
from unittest.mock import patch
from tests.simulation.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):

    # TODO - Need to think of way to create smaller unit tests.
    @patch("tests.simulation.data_handler.os")
    @patch("tests.simulation.data_handler.read_csv")
    def test_get_data(self, mock_pandas_read_csv, mock_os):
        mock_os.listdir.return_value = [
            "test.csv",
            "another_test.csv"
        ]
        mock_pandas_read_csv.return_value = DataFrame.from_dict({
            "date": [1, 2, 3, 4],
            "name": ["sam", "jess", "craig", "aaron"]
        })

        data_handler = DataHandler()
        self.assertEqual(["test.csv", "another_test.csv"], data_handler._DataHandler__test_data_files)


if __name__ == "__main__":
    unittest.main()