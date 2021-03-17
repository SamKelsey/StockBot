import yaml


class ConfigHandler:
    
    def __init__(self, absPath):
        self.absPath = absPath

    # Returns values of config file
    def getConfig(self):        
        
        with open(f'{self.absPath}/config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

        return config
        


if __name__ == '__main__':
    configHandler = ConfigHandler()
    configHandler.getConfig()