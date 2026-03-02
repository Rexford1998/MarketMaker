class SignalEngine:
    def __init__(self, vol_surface):
        self.vol_surface = vol_surface

    def compute_signal(self, symbol):
        # Dummy: sell if IV > 0.2
        chain = self.vol_surface.surface.get(symbol, [])
        signals = []
        for opt in chain:
            if opt["implied_vol"] > 0.2:
                signals.append({"symbol": opt["symbol"], "signal": "SELL"})
        return signals
