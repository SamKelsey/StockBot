import unittest
import sys
import os
print(sys.path)
conf_path = os.getcwd()
sys.path.append(conf_path)
print(sys.path)
from stockBot.StockBot import StockBot

from Alogrithms.simple import Simple

class Tests(unittest.TestCase):
    def test_bot_status(self):
        bot = StockBot()
        self.assertEqual(bot.getStatus(), "running stockBot...")

if __name__ == '__main__':
    unittest.main()