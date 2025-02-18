import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

def train_and_predict(data):
    """Train XGBoost model and track past predictions."""
    data = data.copy()

    # Define features and target
    X = data[['Close', 'Volume', 'SMA_10', 'EMA_10', 'RSI']]
    y = data['Close'].shift(-1).dropna()

    # Align X with y (Fixing inconsistent lengths)
    X = X.iloc[:len(y)]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train XGBoost model
    model = XGBRegressor(n_estimators=100, learning_rate=0.05)
    model.fit(X_train, y_train)

    # Predict on test data to store past predictions
    data.loc[X_test.index, 'Predicted_Close'] = model.predict(X_test)

    # Predict next 5 days' prices
    last_known_features = X.iloc[-1].values.reshape(1, -1)
    predicted_prices = [model.predict(last_known_features)[0]]

    for _ in range(4):
        last_known_features[0][0] = predicted_prices[-1]  # Update "Close" with the last predicted value
        predicted_prices.append(model.predict(last_known_features)[0])

    actual_price_today = data["Close"].iloc[-1]

    # Save past predictions for reference
    data.to_csv("model_predictions.csv", index=True)

    return predicted_prices, actual_price_today, data
