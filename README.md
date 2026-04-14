# Binance Futures Testnet Trading Bot

## Overview

This is a Python CLI-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input
- Input validation
- Logging of requests, responses, and errors
- Error handling for API and validation issues

## Setup

1. Clone the repository

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file:
   BINANCE_API_KEY=your_api_key
   BINANCE_API_SECRET=your_api_secret

## Usage

### MARKET Order

python main.py place-order BTCUSDT BUY MARKET 0.01

### LIMIT Order

python main.py place-order BTCUSDT SELL LIMIT 0.01 --price 80000

## Notes

- Uses Binance Futures Testnet
- Time synchronization handled to avoid timestamp errors
- Logs are stored in `logs/app.log`
