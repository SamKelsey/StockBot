""" A class responsible for handling the money gained/lost over the simulation test """

class BankAccount():

    balance: int

    def __init__(self, starting_balance: int):
        self.balance = starting_balance