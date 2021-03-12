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
            from .Simple import Simple
            return Simple()


class Simple(Algorithm):
    
    def __init__(self):
        print("Created: Simple Algorithm")
    
    def run(self):
        print("Running: Simple Algorithm")