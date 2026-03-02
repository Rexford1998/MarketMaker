class HedgingEngine:
    def __init__(self, broker):
        self.broker = broker

    def hedge_delta(self, symbol, delta):
        if delta == 0:
            return None

        side = "sell" if delta > 0 else "buy"
        order = {
            "symbol": symbol,
            "type": side,
            "size": abs(int(delta)),
            "price": 0,
        }
        return self.broker.place_order(order)
