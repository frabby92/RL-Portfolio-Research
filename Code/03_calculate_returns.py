import pandas as pd
import os

# Load close prices
df = pd.read_csv("Data/close_prices.csv", index_col="Date", parse_dates=True)

print("First 5 rows of prices:")
print(df.head())

# Calculate daily percentage returns
returns = df.pct_change()

# Remove first row (contains NaN)
returns = returns.dropna()

# Create Processed_Data folder
os.makedirs("Data/Processed_Data", exist_ok=True)

# Save returns
returns.to_csv("Data/Processed_Data/daily_returns.csv")

print("\nDaily returns calculated successfully!")

print("\nFirst 5 rows of returns:")
print(returns.head())