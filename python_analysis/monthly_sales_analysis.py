import pandas as pd

df = pd.read_excel(
    r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx"
)

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMONTHLY SALES")
print("=" * 50)

print(monthly_sales.sort_values(ascending=False))