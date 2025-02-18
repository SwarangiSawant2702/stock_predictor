import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data_loader import fetch_stock_data
from indicators import add_technical_indicators
from model import train_and_predict
from sentiment import get_news_sentiment
from visualization import plot_stock

# Streamlit UI
st.title("📈 AI-Based Stock Predictor (XGBoost & LSTM)")

# User input for stock symbol
ticker = st.text_input("Enter Stock Symbol (e.g., AAPL, RELIANCE.NS, TCS.NS)", "AAPL").upper()

# Fetch historical stock data
data = fetch_stock_data(ticker)

if not data.empty:
    st.write(f"Showing historical data for **{ticker}**")
    st.plotly_chart(plot_stock(data))

    # Add technical indicators
    data = add_technical_indicators(data)

    # Train and Predict
    predicted_prices, actual_price_today, predicted_data = train_and_predict(data)
    
    # Display results
    st.subheader("📊 Prediction for Next 5 Days")
    for i, price in enumerate(predicted_prices):
        st.write(f"**Day {i+1}:** ${price:.2f}")

    # Buy/Sell Alert
    if predicted_prices[0] > actual_price_today:
        st.success("📈 Buy Alert! Expected Increase.")
    else:
        st.error("📉 Sell Alert! Expected Drop.")

    # News Sentiment Analysis
    sentiment_score, sentiment_text = get_news_sentiment(ticker)
    if sentiment_score > 0:
        st.success(f"📢 News Sentiment: Positive ({sentiment_text})")
    else:
        st.error(f"📢 News Sentiment: Negative ({sentiment_text})")

    # Display past predictions
    st.subheader("📊 Model's Historical Predictions vs Actual Prices")
    if "Predicted_Close" in predicted_data.columns:
        st.dataframe(predicted_data[['Close', 'Predicted_Close']].dropna().tail(10))  # Show last 10 predictions

else:
    st.warning("⚠ No data available. Check the stock symbol or try again later.")
