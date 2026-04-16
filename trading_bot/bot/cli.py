import click
from bot.client import get_client
from bot.orders import place_order


@click.command()
@click.option("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
@click.option("--side", required=True, type=click.Choice(["BUY", "SELL"], case_sensitive=False))
@click.option("--type", "order_type", required=True,
              type=click.Choice(["MARKET", "LIMIT", "STOP_MARKET"], case_sensitive=False))
@click.option("--quantity", required=True, type=float, help="Order quantity")
@click.option("--price", type=float, help="Limit price (required for LIMIT)")
@click.option("--stop_price", type=float, help="Stop price (required for STOP_MARKET)")
def main(symbol, side, order_type, quantity, price, stop_price):

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol    : {symbol}")
    print(f"Side      : {side}")
    print(f"Type      : {order_type}")
    print(f"Quantity  : {quantity}")
    print(f"Price     : {price}")
    print(f"StopPrice : {stop_price}")

    try:
        # Validation
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if order_type.upper() == "LIMIT" and price is None:
            raise ValueError("LIMIT order requires --price")

        if order_type.upper() == "STOP_MARKET" and stop_price is None:
            raise ValueError("STOP_MARKET requires --stop_price")

        client = get_client()

        order, order_status = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price,
            stop_price
        )

        print("\n========== ORDER SUCCESS ==========")
        print(f"Order ID      : {order['orderId']}")
        print(f"Status        : {order_status['status']}")
        print(f"Executed Qty  : {order_status['executedQty']}")
        print(f"Avg Price     : {order_status.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n========== ERROR ==========")
        print(f"{str(e)}")


if __name__ == "__main__":
    main()