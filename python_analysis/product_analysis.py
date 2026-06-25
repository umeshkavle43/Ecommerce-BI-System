import pandas as pd

df = pd.read_excel(
    r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx"
)

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 50)
print("TOP 10 PRODUCTS")
print("=" * 50)

print(top_products)