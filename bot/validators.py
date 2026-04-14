from decimal import Decimal, InvalidOperation

class ValidationError(Exception):
    pass

class InputValidator:
    VALID_SIDES = {'BUY', 'SELL'}
    VALID_ORDER_TYPES = {'MARKET', 'LIMIT'}
    
    @staticmethod
    def validate_symbol(symbol):
        if not symbol or not symbol.isalnum():
            raise ValidationError(f"Invalid symbol: {symbol}")
        return symbol.upper()
    
    @staticmethod
    def validate_side(side):
        side = side.upper()
        if side not in InputValidator.VALID_SIDES:
            raise ValidationError(f"Side must be BUY or SELL, got: {side}")
        return side
    
    @staticmethod
    def validate_order_type(order_type):
        order_type = order_type.upper()
        if order_type not in InputValidator.VALID_ORDER_TYPES:
            raise ValidationError(f"Order type must be MARKET or LIMIT, got: {order_type}")
        return order_type
    
    @staticmethod
    def validate_quantity(quantity):
        try:
            qty = Decimal(str(quantity))
            if qty <= 0:
                raise ValidationError(f"Quantity must be positive: {quantity}")
            return qty
        except InvalidOperation:
            raise ValidationError(f"Invalid quantity: {quantity}")
    
    @staticmethod
    def validate_price(price, order_type):
        if order_type == 'MARKET':
            return None
        if not price:
            raise ValidationError("Price is required for LIMIT orders")
        try:
            prc = Decimal(str(price))
            if prc <= 0:
                raise ValidationError(f"Price must be positive: {price}")
            return prc
        except InvalidOperation:
            raise ValidationError(f"Invalid price: {price}")
