import yfinance as yf
import os

# Stocks to download
tickers = ["AAPL", "MSFT", "AMZN", "GOOGL", "NVDA"]

# Download data
data = yf.download(
    tickers,
    start="2015-01-01",
    end="2025-01-01",
    auto_adjust=True,
    progress=False
)

# Extract only Close prices
close_prices = data["Close"]

# Create Data folder if needed
os.makedirs("Data", exist_ok=True)

# Save CSV
close_prices.to_csv("Data/close_prices.csv")

print("\nDownload completed successfully!")
print(close_prices.head())
print("\nSaved as Data/close_prices.csv")