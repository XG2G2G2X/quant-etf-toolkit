import numpy as np

def returns(prices):
    return prices.pct_change().dropna()

def annual_volatility(returns, trading_days=252):
    return returns.std() * np.sqrt(trading_days)

def sharpe_ratio(returns, rf=0.0, trading_days=252):
    excess = returns - rf/trading_days
    return (excess.mean() / excess.std()) * np.sqrt(trading_days)
