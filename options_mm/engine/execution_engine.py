class ExecutionEngine:
    def __init__(self, broker):
        self.broker = broker

    def execute_orders(self, orders):
        for order in orders:
            self.broker.place_order(order)
