class MarketData:
    def __init__(self, broker):
        self.broker = broker
        self.data = {}

    def update(self, symbol):
        chain = self.broker.get_options_chain(symbol)
        self.data[symbol] = chain
        return chain
