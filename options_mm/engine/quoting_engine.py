class QuotingEngine:
    def __init__(self, broker):
        self.broker = broker

    def quote(self, signals):
        orders = []
        for signal in signals:
            if signal["signal"] == "SELL":
                orders.append(
                    {
                        "symbol": signal["symbol"],
                        "type": "sell",
                        "size": 10,
                        "price": 100,
                    }
                )
            else:
                orders.append(
                    {
                        "symbol": signal["symbol"],
                        "type": "buy",
                        "size": 10,
                        "price": 95,
                    }
                )
        return orders
