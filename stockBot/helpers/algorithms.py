import abc 
from abc import ABC, abstractmethod

class Algorithm(ABC): 

    @abstractmethod
    def run(self):
        pass


class AlgorithmFactory:

    @staticmethod
    def getAlgorithm(type):
        if (type == "SIMPLE"):
            return Simple()


class Simple(Algorithm):
    
    def __init__(self):
        print("Created: Simple Algorithm")
    
    def run(self, currRow, preRow):
        
        if (currRow > preRow):
            return "Buy"
        elif (currRow < preRow):
            return "Sell"
        else:
            return "Nothing"
        
        print("Running: Simple Algorithm")