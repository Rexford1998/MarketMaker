import random

class SignalsEngine:
    def get_signal(self, symbol):
        # Dummy random signal generator
        return random.choice(["BUY", "SELL", "HOLD"])
