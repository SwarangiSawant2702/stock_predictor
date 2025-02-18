from newsapi import NewsApiClient
from textblob import TextBlob

def get_news_sentiment(ticker):
    """Fetch news articles and analyze sentiment."""
    newsapi = NewsApiClient(api_key="fe988f67b50f4ff8a712513ee8b907a7")  # Replace with your API key
    news = newsapi.get_everything(q=ticker, language="en", sort_by="relevancy")
    
    sentiment_score = 0
    for article in news["articles"][:5]:
        sentiment_score += TextBlob(article["title"]).sentiment.polarity
    
    sentiment_text = "Positive" if sentiment_score > 0 else "Negative"
    return sentiment_score, sentiment_text
