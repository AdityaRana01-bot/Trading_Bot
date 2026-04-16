# Binance Futures Testnet Trading Bot

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Add .env file with API keys
Create a `.env` file based on `.env.example` and add your API credentials.

## Run

Market Order:
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
