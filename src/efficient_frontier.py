import numpy as np
import matplotlib.pyplot as plt

def plot_efficient_frontier(r, C, a, b, d, mean_100k, risk_100k, subset_columns):
    risks = np.sqrt(np.diag(C))
    plt.scatter(risks, r, s=15, label='Assets')
    for i in range(10):
        plt.text(risks[i]+0.0001, r[i], subset_columns[i], size='small')

    opt_mean = mean_100k / 100000
    opt_risk = risk_100k / 100000
    plt.scatter(opt_risk, opt_mean, color='red', s=20, label='Optimal Portfolio')

    mrp_mean = b / a
    mrp_risk = 1 / np.sqrt(a)
    plt.scatter(mrp_risk, mrp_mean, color='green', s=20, label='Min Risk Portfolio')

    ef_mean_range = np.linspace(mrp_mean, 0.01, 100)
    ef_risks = [np.sqrt(1/a + (a/d)*(mu - b/a)**2) for mu in ef_mean_range]
    plt.plot(ef_risks, ef_mean_range, color="purple", label="Efficient Frontier")

    plt.xlabel(r'$\sigma$')
    plt.ylabel(r'$\mu$')
    plt.title(r"$(\sigma,\mu)$ plane")
    plt.legend()
    plt.grid(True)
    plt.show()
