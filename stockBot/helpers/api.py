from binance.client import Client

client = Client()
client.API_URL = "https://testnet.binance.vision/api"

print(client.API_URL)

# get market depth
print(client.get_account())

# from binance.enums import *
# order = client.create_order(
#     symbol='LTCBTC',
#     side="BUY",
#     type="LIMIT",
#     timeInForce="GTC",
#     quantity=100,
#     price='0.001')

