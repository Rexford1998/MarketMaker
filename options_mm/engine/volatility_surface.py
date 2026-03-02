class VolatilitySurface:
    def __init__(self):
        self.surface = {}

    def update_surface(self, symbol, options_chain):
        # Dummy surface: set IV = 0.25 for all strikes
        enriched = []
        for opt in options_chain:
            opt["implied_vol"] = 0.25
            enriched.append(opt)
        self.surface[symbol] = enriched
        return self.surface[symbol]
