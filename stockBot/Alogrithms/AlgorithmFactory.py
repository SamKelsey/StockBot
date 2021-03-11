from .Simple import Simple

class AlgorithmFactory:
    def getAlgorithm(self, type):
        if (type == "SIMPLE"):
            return Simple()