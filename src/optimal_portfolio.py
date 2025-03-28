import numpy as np

def compute_portfolio_parameters(r, C):
    e_vec = np.ones(len(r))
    C_inv = np.linalg.inv(C)

    a = e_vec.T @ C_inv @ e_vec
    b = r.T @ C_inv @ e_vec
    c = r.T @ C_inv @ r
    d = a * c - b**2

    alpha = (1 / a) * (C_inv @ e_vec)
    beta = C_inv @ (r - (b / a) * e_vec)
    return alpha, beta, a, b, c, d

def x_t(alpha, beta, t):
    return alpha + t * beta


def non_short_assets(alpha, beta, columns):
    return [columns[i] for i in range(len(alpha)) if alpha[i] > 0 and beta[i] > 0]