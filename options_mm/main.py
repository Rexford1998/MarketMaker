import time

from engine.execution_engine import ExecutionEngine
from engine.market_data import MarketData
from engine.quoting_engine import QuotingEngine
from engine.risk_engine import RiskEngine
from engine.signal_engine import SignalEngine
from engine.volatility_surface import VolatilitySurface
from infrastructure import redis_state
from infrastructure.broker_adapter import BrokerAdapter

# Initialize
broker = BrokerAdapter()
md = MarketData(broker)
vol = VolatilitySurface()
signals_engine = SignalEngine(vol)
quoting = QuotingEngine(broker)
execution = ExecutionEngine(broker)
risk = RiskEngine(redis_state)

SYMBOLS = ["SPY", "QQQ"]


while True:
    for symbol in SYMBOLS:
        chain = md.update(symbol)
        vol.update_surface(symbol, chain)
        signals = signals_engine.compute_signal(symbol)

        if risk.check_risk(symbol):
            orders = quoting.quote(signals)
            execution.execute_orders(orders)
        else:
            print("Halting trading due to risk limits.")

    time.sleep(5)
