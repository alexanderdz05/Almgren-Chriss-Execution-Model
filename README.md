# Almgren–Chriss Optimal Execution Model

## Project Description

This project implements the Almgren–Chriss Optimal Execution Model for algorithmic trade execution. The goal of the model is to minimize the tradeoff between expected execution cost and execution risk when liquidating or acquiring a large position over time.

The project explores how institutional traders can optimally split large orders into smaller trades while accounting for:
- Temporary market impact
- Permanent market impact
- Price volatility
- Risk aversion

Using historical market data and Monte Carlo simulations, the project compares the Almgren–Chriss strategy against benchmark execution methods such as TWAP (Time Weighted Average Price).

The implementation was completed in Python using Jupyter Notebook with NumPy, Pandas, and Matplotlib. Our historical data was fetched using yfinance.

---

# Table of Contents

- [Project Description](#project-description)
- [Objectives of Project](#objectives-of-project)
- [Project Status & Project Roadmap](#project-status--project-roadmap)
- [Methodology & Workflow](#methodology--workflow)
- [Results & Visuals](#results--visuals)
- [Repository Structure](#repository-structure)
- [Authors & Acknowledgements](#authors--acknowledgements)
- [References](#references)
- [License](#license)

---

# Objectives of Project

1. Understand the mathematical framework behind the Almgren–Chriss model.
2. Model optimal trade execution under market impact and volatility.
3. Generate efficient frontiers between expected cost and execution risk.
4. Compare Almgren–Chriss execution against TWAP strategies.
5. Simulate execution paths using Monte Carlo methods.
6. Analyze the effects of risk aversion on liquidation schedules.
7. Build intuition for market microstructure and execution algorithms.

---

# Project Status & Project Roadmap

This project is currently complete.

The mathematical framework and implementation of the Almgren–Chriss model have been completed. Future work may focus on parameter tuning, additional simulations, and performance visualization. Furthermore, we can implement Chapters 4 (Drift) and 5 (Multiple Securities Portfolios) of the paper.

## Project Status

- **Current Version:** v1.0.0
- **Development Stage:** Core model implementation completed
- **Last Updated:** May 2026

## Project Roadmap

- **Phase 1:** Research Almgren–Chriss optimal execution theory and understand the mathematical framework.
- **Phase 2:** Pull historical data. We chose JPM stock.
- **Phase 3:** Generate simulations and efficient frontier visualizations
- **Phase 4:** Compare against TWAP benchmark strategies
- **Phase 5:** Extend model with more realistic market assumptions

---

# Methodology & Workflow

The project follows the discrete-time Almgren–Chriss framework for optimal execution.

The trader begins with a large inventory position and must optimally execute trades over a finite time horizon. The model balances two competing objectives:

- Minimizing expected execution cost
- Minimizing variance (risk) of execution cost

The optimization is controlled through a risk aversion parameter λ (lambda).

## Methodology

### 1. Market Impact Modeling

The project models:
- Permanent market impact
- Temporary market impact

These components affect the execution price as shares are traded.

### 2. Optimal Liquidation Strategy

Using the Almgren–Chriss closed-form solution, the notebook computes:
- Optimal holdings trajectory
- Optimal trade sizes
- Expected shortfall
- Variance of execution cost

### 3. Efficient Frontier Analysis

Different risk aversion values are tested to generate an efficient frontier showing:
- Lower risk → slower execution
- Higher risk tolerance → faster execution

### 4. Monte Carlo Simulations

Simulated price paths are generated to test strategy robustness under stochastic price movement.

### 5. Benchmark Comparison

The Almgren–Chriss strategy is compared against:
- TWAP execution

Metrics analyzed include:
- Total execution cost
- Risk-adjusted performance
- Trade scheduling behavior

---

# Results & Visuals

The notebook produces multiple visualizations demonstrating the behavior of the optimal execution model.

## Results

Key findings include:

- Higher risk aversion produces smoother and slower liquidation paths.
- Lower risk aversion results in more aggressive execution schedules.
- The efficient frontier demonstrates the tradeoff between expected cost and execution variance.
- Almgren–Chriss generally outperforms naive TWAP execution under modeled market impact assumptions.

### Example Outputs

- Efficient frontier plots
- Inventory decay curves
- Trade execution schedules
- Monte Carlo simulation paths
- Cost vs. risk analysis

## Visuals

### Efficient Frontier

The efficient frontier visualizes the tradeoff between:
- Expected execution cost
- Execution risk (variance)

### Inventory Trajectory

Plots show how inventory decays over time under different λ values.

### Monte Carlo Simulation

Simulated price paths demonstrate how stochastic volatility impacts execution quality.

---

# Repository Structure

```plaintext
project-root/
│
├── almgren-chriss.ipynb     # Main notebook implementation
├── fetch_data.py            # Pulling historical data for JPM
├── jpm_2024.csv             # Historical data for JPM
├── README.md                # Project documentation
└── Optimal Execution of Portfolio Transactions.pdf 
```

## Notes

The primary implementation and analysis are contained within the Jupyter Notebook.

Future improvements may include:
- Changing parameters to try JPM historical data
- Implementing a drift parameter for known events
- Multi-asset execution optimization

---

# Authors & Acknowledgements

## Authors

- **Alexander Dominguez Zhakav**
- **Alisher Raufov**
- **Ty Chan**

## Acknowledgements

Special thanks to:
- Baruch Financial Quants Engineers (FQE)
- Almgren & Chriss for the original research paper

---

# References

1. Almgren, R. & Chriss, N. (2000). *Optimal Execution of Portfolio Transactions*.

---

# License

MIT License

Copyright (c) 2026 Financial Quants & Engineers @ Baruch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
