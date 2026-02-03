

A Python utility library designed for financial market data preprocessing and cost analysis, specifically tailored for Forex (FX) algorithmic trading strategies.

Key Features:

Liquidity Filtering: Functions to isolate specific trading sessions (e.g., London/NY overlap) to ensure strategies only run during high-volume, low-spread hours using Pandas time-series manipulation.

Brokerage Cost Modeling: A module to accurately replicate transaction costs for Pepperstone broker accounts (Razor vs. Standard), handling conversions between pips, spread, and commission fees for backtesting accuracy.

Strategy Analysis: Contains template logic for autocorrelation testing (Mean Reversion) and Moving Average (SMA) crossover strategy implementation.

Tech Stack: Python, Pandas, NumPy, Matplotlib.
