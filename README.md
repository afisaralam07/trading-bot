# Binance Futures Testnet Trading Bot

## Overview

This is a simple Python-based CLI application that allows placing MARKET and LIMIT orders on Binance Futures Testnet.

The goal of this project was to build a clean and functional trading bot with proper structure, input validation, logging, and error handling.

---

## Features

* Place MARKET and LIMIT orders
* Supports both BUY and SELL
* Command-line interface for user input
* Input validation
* Logging of requests, responses, and errors
* Basic error handling for API and network issues

---

## Project Structure

```
trading_bot/

bot/
  client.py
  orders.py
  validators.py
  logging_config.py
  cli.py

logs/
main.py
requirements.txt
README.md
```

---

## Setup

1. Clone the repository
   git clone https://github.com/afisaralam07/trading-bot.git
   cd trading-bot

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Create `.env` file
   Add your Binance Testnet API keys:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

---

## Usage

Market order:
python main.py place-order BTCUSDT BUY MARKET 0.01

Limit order:
python main.py place-order BTCUSDT SELL LIMIT 0.01 --price 80000

---

## Logs

Logs are saved in:
logs/app.log

---

## Notes

* This project uses Binance Futures Testnet
* API keys are stored using environment variables
* Time sync is handled to avoid timestamp errors

---

## Author

Afisar Alam
