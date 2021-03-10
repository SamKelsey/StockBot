import unittest
import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)
from stockBot.StockBot import StockBot

class Tests(unittest.TestCase):
    def test_bot_status(self):
        bot = StockBot()
        self.assertEqual(bot.getStatus(), "running stockBot...")

if __name__ == '__main__':
    unittest.main()