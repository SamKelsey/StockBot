from stockBot.helpers.transaction import Transaction
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from abc import ABC, abstractmethod
from config.config import getConfig
from enum import IntEnum
from dataclasses import dataclass

import threading
import time

class ReceiptStatus(IntEnum):
    SUCCESS = 200
    FAILURE = 500

"""
Describes the outcome of an order that is placed by a broker.
"""
@dataclass
class Receipt():

    status: ReceiptStatus       # Whether the transaction was performed succesfully or not.
    curr_balance: float         # Current bank acc balance.
    total_change: float         # Total change in value in bank acc.

class Broker(ABC):

	@abstractmethod
	def place_order(self, transaction: Transaction) -> Receipt:
		""" Makes an order for some transaction. Returns a receipt. """
		pass

class BrokerFactory:
    @staticmethod
    def getBroker():
        type = getConfig().get("Broker", "BrokerClass")

        if (type == "LiveBroker"):
            return IBapi()

class IBapi(Broker, EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)

	def nextValidId(self, orderId: int):
		super().nextValidId(orderId)
		self.nextorderId = orderId
		print('The next valid order id is: ', self.nextorderId)

	def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
		print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
	
	def openOrder(self, orderId, contract, order, orderState):
		print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action, order.orderType, order.totalQuantity, orderState.status)

	def execDetails(self, reqId, contract, execution):
		print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity)

	def buy(self, tickerInfo):

		# if not isinstance(ticker, list):
		# 	ticker = [ticker]



		def run_loop():
			app.run()

		#Function to create FX Order contract
		def FX_order(symbol, secType = "STK", exchange = "SMART", currency = "USD"):
			contract = Contract()
			contract.symbol = symbol
			contract.secType = secType
			contract.exchange = exchange
			contract.currency = currency
			return contract

		app = IBapi()
		app.connect('127.0.0.1', 7497, 123)

		app.nextorderId = None

		#Start the socket in a thread
		api_thread = threading.Thread(target=run_loop, daemon=True)
		api_thread.start()

		#Check if the API is connected via orderid
		while True:
			if isinstance(app.nextorderId, int):
				print('connected')
				break
			else:
				print('waiting for connection')
				time.sleep(1)

		#Create order object
		def order(action, totalQuantity, orderType = "MKT", lmtPrice = "1.10"):
			order = Order()
			order.action = action
			order.totalQuantity = totalQuantity
			order.orderType = orderType
			order.lmtPrice = lmtPrice

		#Place order
		app.placeOrder(app.nextorderId, FX_order('EURUSD'), order)
		#app.nextorderId += 1

		time.sleep(3)

		#Cancel order 
		# print('cancelling order')
		# app.cancelOrder(app.nextorderId)

		time.sleep(3)
		app.disconnect()



if __name__ == "__main__":
	api = IBapi()