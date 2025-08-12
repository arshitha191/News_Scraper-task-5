import pandas as pd
import matplotlib.pyplot as plt
import os

# Use modern seaborn style from Matplotlib
plt.style.use('seaborn-v0_8')

# CSV file path
csv_file = "sales_data.csv"

# Create CSV automatically if not found
if not os.path.exists(csv_file):
    data = """Date,Product,Region,Sales
2025-01-05,Product A,North,1200
2025-01-08,Product B,South,1500
2025-01-10,Product C,East,900
2025-01-15,Product A,West,1700
2025-02-01,Product B,North,1100
2025-02-04,Product C,South,800
2025-02-06,Product A,East,1600
2025-02-12,Product B,West,1400
2025-03-03,Product C,North,1000
2025-03-07,Product A,South,1800
2025-03-12,Product B,East,1300
2025-03-18,Product C,West,950
"""
    with open(csv_file, "w") as f:
        f.write(data)

# Read CSV
df = pd.read_csv(csv_file)

# Display dataset info
print("First 5 Rows of Dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Grouping & summarizing
sales_by_product = df.groupby("Product")["Sales"].sum().reset_index()
print("\nTotal Sales by Product:")
print(sales_by_product)

sales_by_region = df.groupby("Region")["Sales"].sum().reset_index()
print("\nTotal Sales by Region:")
print(sales_by_region)

# Monthly sales trend
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum().reset_index()
monthly_sales["Date"] = monthly_sales["Date"].astype(str)

# Visualization
plt.figure(figsize=(8,5))
plt.bar(sales_by_product["Product"], sales_by_product["Sales"], color='skyblue')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
plt.bar(sales_by_region["Region"], sales_by_region["Sales"], color='orange')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales["Date"], monthly_sales["Sales"], marker='o', color='green')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()
