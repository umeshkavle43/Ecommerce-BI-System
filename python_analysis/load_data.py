import pandas as pd

# Load Dataset
df = pd.read_excel(r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx")

print("=" * 50)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 50)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())