import pandas as pd
import sys


sys.stdout.reconfigure(encoding='utf-8')


# Load Clean Dataset
df = pd.read_excel(r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx")

print("=" * 50)
print("SALES ANALYSIS")
print("=" * 50)

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print(f"\nTotal Sales: ₹{total_sales:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Total Orders: {total_orders}")

# Top 10 Products
print("\nTop 10 Products by Sales:")
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_products)

# Category Wise Sales
print("\nCategory Wise Sales:")
category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)