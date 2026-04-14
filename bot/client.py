import time
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
from .logging_config import logger
from .validators import ValidationError

load_dotenv()

class BinanceFuturesClient:
    TESTNET_URL = 'https://testnet.binancefuture.com'
    
    def __init__(self):
        self.api_key = os.getenv('BINANCE_API_KEY')
        self.api_secret = os.getenv('BINANCE_API_SECRET')
        
        if not self.api_key or not self.api_secret:
            raise ValidationError("API credentials not found. Check .env file")
        
        try:
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            self.client.FUTURES_URL = self.TESTNET_URL
            
            server_time = self.client.get_server_time()
            system_time = int(time.time() * 1000)
            self.client.timestamp_offset = server_time['serverTime'] - system_time
            
            logger.info("Binance Futures client initialized with time sync")
            
        except Exception as e:
            logger.error(f"Failed to initialize client: {e}")
            raise
    
    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': float(quantity)
            }
            
            if order_type == 'LIMIT':
                params['price'] = float(price)
                params['timeInForce'] = 'GTC'
            
            logger.info(f"Placing order: {params}")
            order = self.client.futures_create_order(**params)
            logger.info(f"Order placed: {order}")
            return order
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise