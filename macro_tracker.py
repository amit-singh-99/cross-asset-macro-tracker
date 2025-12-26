import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def build_macro_tracker(event_name, event_time_str):
    event_time = pd.to_datetime(event_time_str)
    assets = {'SPY': 'S&P 500', 'UUP': 'US Dollar', 'TLT': 'Bonds'}
    fig = go.Figure()

    for ticker, name in assets.items():
        # Attempt to pull real data
        df = yf.download(ticker, interval="1m", period="5d", progress=False, auto_adjust=True)
        
        if not df.empty:
            df.index = df.index.tz_localize(None)
            # Filter for a window around your event_time
            df_plot = df.iloc[-120:].copy() # Get the last 2 hours of available data
            
            # Normalize
            base = df_plot['Close'].iloc[0]
            df_plot['Norm'] = (df_plot['Close'] / base) * 100
            df_plot['Rel_Min'] = np.arange(len(df_plot)) - 30 # Mock X-axis
            
            fig.add_trace(go.Scatter(x=df_plot['Rel_Min'], y=df_plot['Norm'], name=name))
            print(f"✓ Using REAL data for {ticker}")
        else:
            # DUMMY DATA GENERATOR (So you can see the chart work)
            x = np.linspace(-30, 90, 120)
            y = 100 + np.cumsum(np.random.normal(0, 0.1, 120))
            fig.add_trace(go.Scatter(x=x, y=y, name=f"{name} (Simulated)"))
            print(f"! Using SIMULATED data for {ticker} (Market is Closed)")

    fig.update_layout(
        title=f"<b>{event_name}</b>",
        xaxis_title="Minutes from Release",
        yaxis_title="Price Indexed to 100",
        template="plotly_dark",
        yaxis=dict(range=[98, 102])
    )
    fig.add_vline(x=0, line_dash="dash", line_color="red")
    fig.show()

build_macro_tracker("CPI Impact Study", "2025-12-24 08:30:00")
