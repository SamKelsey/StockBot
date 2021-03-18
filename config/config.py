import os
from configparser import ConfigParser

def getConfig():
    configParser = ConfigParser()   
    
    if (os.getenv('PYTHON_ENV') == 'test'):
        configFilePath = 'config/test-config.ini'
        configParser.read(configFilePath)
        return configParser
    elif (os.getenv('PYTHON_ENV') == 'dev'):
        configFilePath = 'config/dev-config.ini'
        configParser.read(configFilePath)
        return configParser