# Options Market Maker Skeleton

## 1) Project structure

```text
/options_mm
    /engine
        market_data.py
        volatility_surface.py
        greeks_engine.py
        signal_engine.py
        quoting_engine.py
        execution_engine.py
        hedging_engine.py
        risk_engine.py
    /infrastructure
        broker_adapter.py
        redis_state.py
        db.py
        logging.py
    /dashboard
        web_app.py
    /tests
        backtest_engine.py
        stress_tests.py
    main.py
```

- `engine/` – Core trading logic
- `infrastructure/` – Broker, database, Redis, logging
- `dashboard/` – Web monitoring
- `tests/` – Backtesting & stress tests
- `main.py` – Orchestrates everything

## 2) Install required packages (AWS/local)

```bash
sudo apt update
sudo apt install python3-pip python3-venv git
pip install numpy pandas scipy redis sqlalchemy fastapi uvicorn apscheduler
```

Optional for local IDE development: VS Code + Python extension.
