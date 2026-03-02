import time
from engine import risk_engine, signals_engine, broker_adapter
from infrastructure import redis_state

# Define your trading symbols
symbols = ["SPY", "QQQ"]

# Initialize engines
risk = risk_engine.RiskEngine()
signals = signals_engine.SignalsEngine()
broker = broker_adapter.DummyBroker()

print("=== Market Making Engine Starting ===", flush=True)

# Main loop
while True:
    for symbol in symbols:
        print(f"[DEBUG] Checking risk for {symbol}", flush=True)
        if risk.check_risk(symbol):
            signal = signals.get_signal(symbol)
            print(f"[DEBUG] Signal for {symbol}: {signal}", flush=True)
            
            if signal != "HOLD":
                print(f"[DEBUG] Sending order for {symbol}: {signal}", flush=True)
                broker.place_order(symbol, signal)
                # Update position in Redis
                redis_state.set_position(symbol, broker.get_position(symbol))
            else:
                print(f"[DEBUG] No trade for {symbol}, HOLD signal", flush=True)
        else:
            print(f"[DEBUG] Risk check failed for {symbol}, skipping trade", flush=True)

    # Sleep between loops to prevent busy CPU
    time.sleep(1)
