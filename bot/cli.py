import click
from .orders import OrderManager
from .logging_config import logger

@click.group()
def cli():
    """Trading Bot CLI"""
    pass

@cli.command()
@click.argument('symbol')
@click.argument('side', type=click.Choice(['BUY', 'SELL']))
@click.argument('order_type', type=click.Choice(['MARKET', 'LIMIT']))
@click.argument('quantity')
@click.option('--price', '-p', help='Price for LIMIT orders')
def place_order(symbol, side, order_type, quantity, price):
    """Place an order"""
    try:
        manager = OrderManager()
        
        click.echo("\\n" + "="*60)
        click.echo("ORDER REQUEST")
        click.echo("="*60)
        click.echo(f"Symbol: {symbol}")
        click.echo(f"Side: {side}")
        click.echo(f"Type: {order_type}")
        click.echo(f"Quantity: {quantity}")
        if price:
            click.echo(f"Price: {price}")
        
        if not click.confirm("\\nProceed?"):
            click.echo("Cancelled")
            return
        
        result = manager.place_order(symbol, side, order_type, quantity, price)
        
        if result['success']:
            click.echo("\\n✅ SUCCESS!")
            click.echo(f"Order ID: {result['order_id']}")
            click.echo(f"Status: {result['status']}")
        else:
            click.echo(f"\\n❌ FAILED: {result['error']}")
            
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
