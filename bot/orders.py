from .client import BinanceFuturesClient
from .validators import InputValidator, ValidationError
from .logging_config import logger

class OrderManager:
    def __init__(self):
        self.client = BinanceFuturesClient()
        logger.info("OrderManager initialized")
    
    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info("Validating inputs...")
            validated = {
                'symbol': InputValidator.validate_symbol(symbol),
                'side': InputValidator.validate_side(side),
                'order_type': InputValidator.validate_order_type(order_type),
                'quantity': InputValidator.validate_quantity(quantity),
                'price': InputValidator.validate_price(price, order_type)
            }
            
            logger.info(f"Inputs validated: {validated}")
            
            order_response = self.client.place_order(
                symbol=validated['symbol'],
                side=validated['side'],
                order_type=validated['order_type'],
                quantity=float(validated['quantity']),
                price=float(validated['price']) if validated['price'] else None
            )
            
            return {
                'success': True,
                'order_id': order_response.get('orderId'),
                'status': order_response.get('status'),
                'symbol': order_response.get('symbol'),
                'side': order_response.get('side'),
                'executed_qty': order_response.get('executedQty'),
                'avg_price': order_response.get('avgPrice')
            }
            
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            return {'success': False, 'error': str(e)}
        except Exception as e:
            logger.error(f"Order failed: {e}")
            return {'success': False, 'error': str(e)}
