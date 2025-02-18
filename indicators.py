import pandas as pd

def compute_rsi(series, period=14):
    """Calculate Relative Strength Index (RSI)."""
    delta = series.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def add_technical_indicators(data):
    """Add technical indicators to stock data."""
    data["SMA_10"] = data["Close"].rolling(window=10).mean()
    data["EMA_10"] = data["Close"].ewm(span=10, adjust=False).mean()
    data["RSI"] = compute_rsi(data["Close"])
    data.dropna(inplace=True)
    return data
