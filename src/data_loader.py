import yfinance as yf
import pandas as pd

def load_data(tickers, start="2015-01-01"):
    data = yf.download(tickers, start=start)["Adj Close"]
    return data
