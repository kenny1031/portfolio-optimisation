import numpy as np

def compute_returns(data):
    subset = data.iloc[:, 1:]
    returns = (subset / subset.shift(1) - 1).dropna()
    return returns

def compute_statistics(returns):
    r = np.mean(returns.T.to_numpy(), axis=1).round(6)
    C = np.cov(returns.T).round(6)
    return r, C