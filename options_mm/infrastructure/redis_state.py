import redis
import json

# Connect to local Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def set_position(symbol, position):
    r.set(f"position:{symbol}", json.dumps(position))

def get_position(symbol):
    pos = r.get(f"position:{symbol}")
    return json.loads(pos) if pos else 0
