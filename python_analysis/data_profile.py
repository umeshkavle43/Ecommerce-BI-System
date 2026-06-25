import pandas as pd

df = pd.read_excel(r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())