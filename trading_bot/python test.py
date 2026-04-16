from binance.client import Client
import os
import time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

# ✅ Correct testnet futures URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# ✅ Fix timestamp issue
server_time = client.get_server_time()
client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)

# ✅ Test API
balance = client.futures_account_balance()

print("CONNECTED SUCCESSFULLY ✅")
print(balance)

# Place test order
order = client.futures_create_order(
    symbol="BTCUSDT",
    side="BUY",
    type="MARKET",
    quantity=0.001
)

time.sleep(2)

client.futures_get_order(
    symbol="BTCUSDT",
    orderId=order['orderId']
)

print("ORDER PLACED ✅")
print(order)
order_status = client.futures_get_order(
    symbol="BTCUSDT",
    orderId=order['orderId']
)

print("ORDER STATUS:", order_status)