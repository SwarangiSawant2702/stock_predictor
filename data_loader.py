import yfinance as yf

def fetch_stock_data(ticker):
    """Fetch historical stock data from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    data = stock.history(period="2y")
    return data
