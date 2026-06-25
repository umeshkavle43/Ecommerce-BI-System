import pandas as pd

# Load Dataset
df = pd.read_excel(r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx")

print("Original Shape:", df.shape)

# Remove Duplicates
df = df.drop_duplicates()

print("After Removing Duplicates:", df.shape)

# Convert Date Columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Create New Columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()

# Save Clean Dataset
df.to_excel(r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")