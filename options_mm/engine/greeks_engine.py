import math


def black_scholes_greeks(S, K, T, r, sigma, option_type="call"):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    # Simplified, just returns delta
    delta = 0.5  # placeholder
    return {"delta": delta, "gamma": 0, "vega": 0, "theta": 0, "d1": d1, "d2": d2}
