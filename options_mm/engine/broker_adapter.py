from infrastructure import redis_state

class DummyBroker:
    def __init__(self):
        self.positions = {}

    def place_order(self, symbol, side):
        pos = self.positions.get(symbol, 0)
        if side == "BUY":
            pos += 1
        elif side == "SELL":
            pos -= 1
        self.positions[symbol] = pos
        print(f"[BROKER] Updated position for {symbol}: {pos}", flush=True)

    def get_position(self, symbol):
        return self.positions.get(symbol, 0)
