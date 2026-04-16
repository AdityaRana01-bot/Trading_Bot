import time


def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):

    # Normalize input
    order_type = order_type.upper().strip()
    side = side.upper().strip()

    if order_type == "MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    elif order_type == "LIMIT":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

    elif order_type == "STOP_MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",
            stopPrice=stop_price,
            quantity=quantity
        )

    else:
        raise ValueError(f"Invalid order type: {order_type}")

    # Wait for Binance to update order status
    time.sleep(1)

    # Fetch updated order status
    order_status = client.futures_get_order(
        symbol=symbol,
        orderId=order["orderId"]
    )

    return order, order_status