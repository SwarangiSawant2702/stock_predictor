# AI-Based Stock Predictor

## Overview
This project is an **AI-powered stock predictor** using **Streamlit**, **XGBoost**, and **Yahoo Finance data**. The application fetches real-time stock data, applies technical indicators, and predicts future prices using machine learning.

## Features
- **Fetch Historical Stock Data**: Uses Yahoo Finance API to retrieve stock prices.
- **Technical Indicators**: Computes SMA, EMA, and RSI.
- **Stock Price Prediction**: Implements an XGBoost model to forecast prices for the next 5 days.
- **Sentiment Analysis**: Analyzes news sentiment using NewsAPI and TextBlob.
- **Interactive Visualization**: Displays stock trends using Plotly.
- **Buy/Sell Alert**: Provides trade recommendations based on predictions.

## Installation
### **1. Clone the Repository**
```bash
 git clone https://github.com/your-repo/stock-predictor.git
 cd stock-predictor
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Up API Keys**
- **Yahoo Finance**: No API key required.
- **NewsAPI**: Set up an environment variable for secure access:
```bash
export NEWS_API_KEY="your_newsapi_key"
```
To obtain a NewsAPI key, sign up at [NewsAPI.org](https://newsapi.org) and generate an API key.

## Usage
### **Run the Streamlit App**
```bash
streamlit run app.py
```

## File Structure
- `app.py` - Streamlit UI and integration of all modules.
- `data_loader.py` - Fetches historical stock data from Yahoo Finance.
- `indicators.py` - Computes technical indicators (SMA, EMA, RSI).
- `model.py` - Trains an XGBoost model and predicts stock prices.
- `sentiment.py` - Fetches news and analyzes sentiment using NewsAPI.
- `visualization.py` - Generates stock charts using Plotly.

## Future Improvements
- **Integrate LSTM Model**: Add deep learning-based predictions.
- **Enhance Feature Set**: Use macroeconomic indicators.
- **Improve Sentiment Analysis**: Use NLP models like VADER or BERT.

## License
This project is open-source under the MIT License.

---
📌 **Note**: Ensure that API keys are properly secured before deploying.

