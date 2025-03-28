import numpy as np

def compute_betas(r, C, x_M):
    market_return = x_M @ r
    market_variance = x_M.T @ C @ x_M
    betas = (C @ x_M) / market_variance
    return betas