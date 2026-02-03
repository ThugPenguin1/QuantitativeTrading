from os import access

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import backtest as bt




# Load the data (adjust filename to match yours)



def load_csv(filepath):
    """Load saved CSV format"""
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    return df
def df_trading_hours(df, trading_num=1):
    """
    Filter dataframe to specific trading hours.

    Parameters:
    -----------
    df : DataFrame with DateTime index
    trading_num : int
        1 = Conservative (13:00 - 17:00 UTC) - London/NY overlap
        2 = Moderate (08:00 - 20:00 UTC) - Full active session

    Returns:
    --------
    DataFrame filtered to specified hours
    """
    df = df.copy()  # Avoid modifying original
    df['Hour'] = df.index.hour

    if trading_num == 1:
        # Conservative: 13:00 - 17:00 UTC
        df_liquid = df[(df['Hour'] >= 13) & (df['Hour'] <= 16)]  # 16 means up to 16:59
    elif trading_num == 2:
        # Moderate: 08:00 - 20:00 UTC
        df_liquid = df[(df['Hour'] >= 8) & (df['Hour'] <= 19)]  # 19 means up to 19:59
    else:
        df_liquid = df  # Return all data if invalid number

    # Optional: drop the Hour column we added
    df_liquid = df_liquid.drop(columns=['Hour'])

    return df_liquid
def pepperstone_replication(account_type):
    """
    SETTINGS FOR PEPPERSTONE REPLICATION


    Input: (1 or 2)
    ACCOUNT TYPE: 1 = RAZOR, 2 = STANDARD
    RAZOR: has raw spread + comission
    STANDARD: has spread only

    Output:
    float: total cost per trip
    """
    if account_type == 1: # Razor account
        spread_pips = 0.1 # on average its like that
        commission_usd_roundtrip = 7.00 # enter and exit the trade it averages 7

    elif account_type == 2:
        spread_pips = 1.0
        commission_usd_roundtrip = 0


    # convert pips to dec
    spread_decimal = spread_pips * 0.0001
    commission_decimal = commission_usd_roundtrip / 100000

    total_cost = spread_decimal + commission_decimal
    return total_cost








"""df['Return_1m'] = df['Close'].pct_change()
df['Return_1h'] = df['Close'].pct_change(60)
df['Return_1d'] = df['Close'].pct_change(1440)

# Check autocorrelation (negative = mean reverting, positive = momentum)
print("=== AUTOCORRELATION (Negative = Mean Reverting) ===")
for lag in [1, 5, 10, 30, 60]:
    autocorr = df['Return_1m'].autocorr(lag=lag)
    print(f"Lag {lag} minutes: {autocorr:.4f}")
    
# This checks if EURUSD is mean reverting or momentum 
    """




"""# Parse the datetime
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%Y%m%d %H%M%S')
df.set_index('DateTime', inplace=True)

df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()

# Generate signals
df['Signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1   # Buy signal
df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1  # Sell signal

# Calculate returns
df['Price_Return'] = df['Close'].pct_change()
df['Strategy_Return'] = df['Signal'].shift(1) * df['Price_Return']

# Calculate cumulative returns
df['Cumulative_Market'] = (1 + df['Price_Return']).cumprod()
df['Cumulative_Strategy'] = (1 + df['Strategy_Return']).cumprod()

# Plot comparison
df[['Cumulative_Market', 'Cumulative_Strategy']].plot(figsize=(12, 6))
plt.title('Strategy vs Buy & Hold')
plt.show()

# Basic stats
total_return = df['Cumulative_Strategy'].iloc[-1] - 1
print(f"Total Strategy Return: {total_return:.2%}")


"""







"""
# Calculate 20-period and 50-period SMAs
df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()

# Plot them together
df[['Close', 'SMA_20', 'SMA_50']].tail(1000).plot(figsize=(12, 6))
plt.title('EUR/USD with Moving Averages')
plt.show()
"""


"""
# Check what you have
print(df.head())
print(f"\nTotal rows: {len(df)}")
print(f"Date range: {df.index.min()} to {df.index.max()}")
"""

"""
# Plot the close price
df['Close'].plot(figsize=(12, 6), title='EUR/USD Close Price')
plt.show()
"""

