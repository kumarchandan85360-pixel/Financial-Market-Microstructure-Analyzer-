import numpy as np
import pandas as pd

# Create market data
df = pd.DataFrame({
    "Time": pd.date_range("09:30", periods=8, freq="1min"),
    "Bid_Price": [100.0, 100.2, 100.1, 100.3, 100.4, 100.6, 100.7, 100.8],
    "Ask_Price": [100.5, 100.6, 100.55, 100.7, 100.9, 101.0, 101.1, 101.2],
    "Trade_Price": [100.2, 100.3, 100.4, 100.6, 100.7, 100.8, 101.0, 101.1],
    "Volume": [200, 180, 250, 300, 400, 350, 500, 450]
})

# Convert to NumPy arrays
bid = df["Bid_Price"].to_numpy()
ask = df["Ask_Price"].to_numpy()
trade = df["Trade_Price"].to_numpy()
volume = df["Volume"].to_numpy()

# Microstructure calculations
df["Bid_Ask_Spread"] = ask - bid
df["Mid_Price"] = (ask + bid) / 2
df["Returns"] = np.insert(np.diff(trade) / trade[:-1], 0, np.nan)
df["Liquidity"] = volume / df["Bid_Ask_Spread"]

# Summary statistics
summary = pd.DataFrame({
    "Average Spread": [np.mean(df["Bid_Ask_Spread"])],
    "Max Price": [np.max(trade)],
    "Min Price": [np.min(trade)],
    "Total Volume":
))
