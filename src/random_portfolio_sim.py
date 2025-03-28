import numpy as np
import matplotlib.pyplot as plt

def generate_random_portfolios(n, r, C):
    weights = np.random.dirichlet(np.ones(len(r)), n)
    portfolio_returns = weights @ r
    portfolio_risks = np.sqrt(np.einsum('ij,jk,ik->i', weights, C, weights))
    return weights, portfolio_returns, portfolio_risks

def plot_random_portfolios(portfolio_risks, portfolio_returns):
    plt.scatter(portfolio_risks, portfolio_returns, color='gray', s=1, label='Feasible Portfolios')
    plt.xlabel(r'$\sigma$')
    plt.ylabel(r'$\mu$')
    plt.title('Random Feasible Portfolios in $(\sigma,\mu)$ plane')
    plt.grid(True)
    plt.legend()
    plt.show()

def distance_to_mrp(weights, C):
    mrp = np.linalg.solve(C, np.ones(C.shape[0]))
    mrp /= np.sum(mrp)
    dist = np.linalg.norm(weights - mrp, axis=1)
    return dist, mrp

def loglog_plot_proximity(dist):
    delta_range = np.logspace(-1, 1, 100)
    proportions = [np.mean(dist < delta) for delta in delta_range]
    plt.loglog(delta_range, proportions, marker='o', color='b', label=r'$P(d_i < \delta)$')
    plt.xlabel(r'$\delta$')
    plt.ylabel(r'$P(d_i < \delta)$')
    plt.title('Proximity to Minimum Risk Portfolio')
    plt.grid(True)
    plt.legend()
    plt.show()