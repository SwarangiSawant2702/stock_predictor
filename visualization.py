import plotly.graph_objects as go

def plot_stock(data):
    """Generate a stock price chart using Plotly."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title='Stock Price Movement', xaxis_title='Date', yaxis_title='Close Price')
    return fig
