import os 
import sys 
print(sys.path)
if __name__ == '__main__':
    from Alogrithms.simple import Simple
else:
    from stockBot.Alogrithms.simple import Simple


x = Simple()
x.run()


