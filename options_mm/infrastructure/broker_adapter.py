class BrokerAdapter:
    def __init__(self):
        # Initialize FIX or REST connection here
        pass

    def get_options_chain(self, symbol):
        # Replace with real API call
        return []

    def place_order(self, order):
        # order = {"symbol": ..., "type": "buy/sell", "size":..., "price":...}
        print(f"Placing order: {order}")
        return {"status": "submitted", "order_id": 123}

    def get_fills(self):
        # Returns fills from broker
        return []
