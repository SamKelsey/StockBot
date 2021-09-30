from stockBot.helpers.brokers import Broker, Receipt
from stockBot.helpers.transaction import Transaction

""" A class responsible for handling the money gained/lost over the simulation test """
class TestBroker(Broker):

    balance: int

    def __init__(self, starting_balance: int):
        self.balance = self.starting_balance = starting_balance

    def place_order(self, transaction: Transaction) -> Receipt:
        pass

if __name__ == "__main__":
    acc = Broker(100)
