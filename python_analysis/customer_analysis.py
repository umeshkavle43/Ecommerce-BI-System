import pandas as pd

df = pd.read_excel(
   r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx"
)

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 50)
print("TOP 10 CUSTOMERS")
print("=" * 50)

print(top_customers)