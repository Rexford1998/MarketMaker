from infrastructure import redis_state

class RiskEngine:
    def check_risk(self, symbol):
        # Simple example: always allow trade if current position < 10
        pos = redis_state.get_position(symbol)
        print(f"[RISK] Current position for {symbol}: {pos}", flush=True)
        return abs(pos) < 10
