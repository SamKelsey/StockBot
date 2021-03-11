import os 
import sys 
conf_path = os.getcwd()
sys.path.append(conf_path)

from stockBot.Alogrithms.simple import Simple

class StockBot:
    def getStatus():
        return "running stockBot..."

x = Simple()
x.run()


