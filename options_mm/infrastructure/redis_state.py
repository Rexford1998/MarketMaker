# infrastructure/redis_state.py

import redis
import json

# Change this:
# r = redis.Redis(host='your-redis-endpoint', port=6379, db=0)

# To this for local testing:
r = redis.Redis(host='localhost', port=6379, db=0)

def set_position(symbol, position):
    r.set(f"position:{symbol}", json.dumps(position))

def get_position(symbol):
    pos = r.get(f"position:{symbol}")
    return json.loads(pos) if pos else None
