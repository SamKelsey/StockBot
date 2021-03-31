from config.config import getConfig
from stockBot.helpers.api import IBapi

class BrokerFactory:
    @staticmethod
    def getBroker():
        type = getConfig().get("Broker", "BrokerClass")

        if (type == "LiveBroker"):
            return IBapi()