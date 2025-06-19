import pandas as pd
import matplotlib.pyplot as plt


# Load data
df = pd.read_csv("Sales Data.csv")

# First 5 rows
print(df.head())

# Basic stats
print(df.describe())

# Check missing values
print(df.isnull().sum())
# data cleaning
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["City"] = df["City"].str.strip()


# 1. Monthly Sales Trend
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.xticks(range(1, 13))
plt.tight_layout()
plt.show()
