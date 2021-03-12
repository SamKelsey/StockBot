import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)

import unittest
from stockBot.StockBot import StockBot
from stockBot.algorithms_package.algorithms import Simple

class Tests(unittest.TestCase):
    def test_bot_status(self):
        bot = StockBot()
        self.assertEqual(bot.getStatus(), "Running: Stockbot")

    def test_bot_running(self):
        bot = StockBot()
        self.assertEqual(bot.startBot(), "Starting: Stockbot")

if __name__ == '__main__':
    unittest.main()