from stockBot.helpers.transaction import Transaction
from dataclasses import dataclass
from enum import IntEnum

class Status(IntEnum):
    SUCCESS = 200
    FAILURE = 500

@dataclass
class Receipt():

    status: Status              # Whether the transaction was performed succesfully or not.
    curr_balance: float         # Current bank acc balance.
    total_change: float         # Total change in value in bank acc.

""" A class responsible for handling the money gained/lost over the simulation test """
class BankAccount():

    balance: int

    def __init__(self, starting_balance: int):
        self.balance = self.starting_balance = starting_balance

    """
    @desc       Performs the necessary steps for a given transaction
    @args       - transaction: A Transaction object
    @returns    - receipt: A Receipt object
    """
    def perform(self, transaction: Transaction) -> Receipt:
        pass

if __name__ == "__main__":
    acc = BankAccount(100)
