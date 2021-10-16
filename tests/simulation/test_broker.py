from stockBot.helpers.brokers import Broker, BrokerException, Receipt, ReceiptStatus
from stockBot.helpers.transaction import Transaction, Action
import logging

logger = logging.getLogger()

""" A class responsible for handling the money gained/lost over the simulation test """
class TestBroker(Broker):

    balance: int                # Total balance of account.
    portfolio: dict             # Map of units of stock owned per ticker.

    def __init__(self, starting_balance: int):
        self.balance = starting_balance
        self.portfolio = {}

    
    def place_order(self, transaction: Transaction) -> Receipt:
        switches = {
            Action.BUY: self.buy_stock,
            Action.SELL: self.sell_stock
        }
        
        func = switches.get(
            transaction.action, 
            lambda self : "Doing nothing"
        )

        func(transaction)
        return Receipt(ReceiptStatus.SUCCESS, 100, 10)

    """ 
    @desc       Returns the total value of assets owned (stock + cash)
    @args       - stock_price: A float of the current price of the stock owned.
    @returns    - Float value of total assets owned.
    """
    def get_total_equity(self, stock_price: float):
        stock_assets = next(iter(self.portfolio.values())) * stock_price['Close']
        return stock_assets + self.balance

    def buy_stock(self, transaction: Transaction):

        # Check there are adequate funds in balance.
        if (transaction.get_total_price() > self.balance):
            raise BrokerException("Insufficient funds.")

        # Deduct total cost of stock from balance.
        self.balance = self.balance - transaction.get_total_price()

        # Add key-value to a dictionary showing how many units of stock are owned.
        self.portfolio[transaction.stock_ticker] = \
            self.portfolio.get(transaction.stock_ticker, 0) + transaction.stock_qty

        logger.info(f"Bought {transaction.stock_ticker}. Current balance: {round(self.balance, 2)}")

    def sell_stock(self, transaction: Transaction):

        # Check there is adequate equity owned in that stock.
        if ((not transaction.stock_ticker in self.portfolio) or (self.portfolio[transaction.stock_ticker] < transaction.stock_qty)):
            raise BrokerException("Insufficient stock.")

        # Add total value of that sale to balance.
        self.balance = self.balance + transaction.get_total_price()

        # Subtract quantity of stock from dict.
        self.portfolio[transaction.stock_ticker] = \
            self.portfolio[transaction.stock_ticker] - transaction.stock_qty

        logger.info(f"Sold {transaction.stock_ticker}. Current balance: {round(self.balance, 2)}")

if __name__ == "__main__":
    acc = TestBroker(10000)

    transaction = Transaction(Action.SELL, 400, 10, "AAPL")

    acc.place_order(transaction)
