from src.load_data import load_stock_data
from src.compute_returns import compute_returns, compute_statistics
from src.optimal_portfolio import compute_portfolio_parameters, non_short_assets
from src.investor_analysis import investor_stats
from src.efficient_frontier import plot_efficient_frontier
from src.capm_analysis import compute_betas
from src.random_portfolio_sim import (
    generate_random_portfolios,
    plot_random_portfolios,
    distance_to_mrp,
    loglog_plot_proximity,
)
import numpy as np

if __name__ == "__main__":
    data = load_stock_data("data/project_data.csv")
    subset_columns = data.columns[1:]
    returns = compute_returns(data)
    r, C = compute_statistics(returns)

    alpha, beta, a, b, c, d = compute_portfolio_parameters(r, C)

    print("Non-short-sold assets:")
    print(non_short_assets(alpha, beta, subset_columns))

    t = 0.06
    total = 100000
    allocation, mean_return, risk = investor_stats(alpha, beta, a, b, d, t, total)

    print("\nOptimal allocation ($):")
    print(allocation.round(2))
    print("Mean return ($):", round(mean_return, 2))
    print("Risk ($):", round(risk, 2))

    plot_efficient_frontier(r, C, a, b, d, mean_return, risk, subset_columns)

    x_M = np.array([0.191, 0.187, 0.116, 0.095, 0.088, 0.075, 0.072, 0.065, 0.06, 0.051])
    betas = compute_betas(r, C, x_M)
    print("\nBetas:")
    for name, beta in zip(subset_columns, betas):
        print(f"{name}: {beta:.6f}")

    weights, port_returns, port_risks = generate_random_portfolios(10000, r, C)
    plot_random_portfolios(port_risks, port_returns)

    dist, mrp = distance_to_mrp(weights, C)
    loglog_plot_proximity(dist)