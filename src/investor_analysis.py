import numpy as np

def investor_stats(alpha, beta, a, b, d, t, total):
    weights = alpha + t * beta
    allocation = weights * total
    mean_return = (b + d * t) / a * total
    var = (1 + d * t**2) / a
    risk = np.sqrt(var) * total
    return allocation, mean_return, risk
