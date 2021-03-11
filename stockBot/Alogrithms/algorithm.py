import abc 
from abc import ABC, abstractmethod

class Algorithm(ABC): 

    @abstractmethod
    def run(self):
        pass

