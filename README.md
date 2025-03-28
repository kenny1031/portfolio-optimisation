# 📈 Portfolio Optimisation and Financial Mathematics

This project implements a full analysis pipeline for portfolio optimisation using real stock data from the Australian Stock Exchange (ASX). It includes classical Markowitz optimisation, CAPM beta analysis, and efficient frontier visualisation — built from scratch in Python.

## 📊 Project Overview

This project showcases:

- 📁 Return & covariance matrix computation  
- 🧮 Optimal portfolio construction for arbitrary risk aversion  
- 💰 Investment strategy for $100,000  
- 📐 Efficient frontier & minimum variance frontier plots  
- 💼 CAPM beta analysis for ASX stocks  
- 🔄 Random portfolio simulations & high-dimensional proximity analysis

---

## 🗂️ Project Structure
```bash
portfolio-optimisation/
│
├── data/
│   └── project_data.csv
│
├── src/
│   ├── load_data.py              # Loads and preprocesses the dataset
│   ├── compute_returns.py        # Computes returns, mean vector, and covariance matrix
│   ├── optimal_portfolio.py      # Solves for optimal portfolio x(t), α, β
│   ├── investor_analysis.py      # Performs analysis for specific investor settings
│   ├── efficient_frontier.py     # Plots frontiers and portfolios
│   ├── capm_analysis.py          # Computes betas and market risk relationships
│   ├── random_portfolio_sim.py   # Generates random portfolios and analyses them
│
├── main.py                       # Runs all analysis together
├── README.md                     # Description of project and setup
└── requirements.txt              # Libraries needed (e.g., numpy, pandas, matplotlib, scipy)
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kenny1031/portfolio-optimisation.git
cd portfolio-optimisation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis

```bash
python3 main.py
```

## 📁 Data Source

The dataset (`project_data.csv`) includes end-of-day adjusted stock prices for the 10 largest ASX companies from 1 July 2022 to 30 June 2024, excluding dividend effects.

## 🧠 Concepts Used

* Markowitz Mean-Variance Optimisation
* Efficient Frontier and Minimum Variance Portfolio
* Capital Market Line (CML)
* Capital Asset Pricing Model (CAPM)
* Portfolio Simulation in High Dimensions

## 🙋‍♂️ Author

Kunda Yu
Computer Science and Mathematics @ The University of Sydney