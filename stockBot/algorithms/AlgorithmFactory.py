class AlgorithmFactory:
    def getAlgorithm(self, type):
        if (type == "SIMPLE"):
            from .Simple import Simple
            return Simple()