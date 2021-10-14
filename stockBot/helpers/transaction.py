from dataclasses import dataclass
from enum import IntEnum


"""
Integar enums to describe a transaction's purchasing action.
"""
class Action(IntEnum):
    BUY = 0
    SELL = 1
    NOTHING = 2

"""
Used by Brokers to perform purchasing actions
"""
@dataclass
class Transaction():
    
    action: Action          # To buy/sell/nothing.
    stock_ticker: str = ''  # Ticker of the stock.
    stock_qty: int = 0      # Quantity of stocks to perform action on.
    stock_price: float = 0  # Price of a single stock at time of transaction.

    def get_total_price(self) -> float:
        return self.stock_price * self.stock_qty