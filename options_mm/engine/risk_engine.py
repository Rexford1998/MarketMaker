class RiskEngine:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.max_delta = 500

    def check_risk(self, symbol):
        pos = self.redis.get_position(symbol) or 0
        if abs(pos) > self.max_delta:
            print("Risk limit breached! Kill switch activated.")
            return False
        return True
