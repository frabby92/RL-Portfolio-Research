import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
df = pd.read_csv("Data/close_prices.csv", index_col="Date", parse_dates=True)

# Create Figures folder
os.makedirs("Figures", exist_ok=True)

# Basic information
print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# Plot stock prices
plt.figure(figsize=(12,6))

for stock in df.columns:
    plt.plot(df.index, df[stock], label=stock)

plt.title("Daily Closing Prices (2015-2025)")
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price")
plt.legend()

plt.savefig("Figures/stock_prices.png")
plt.show()