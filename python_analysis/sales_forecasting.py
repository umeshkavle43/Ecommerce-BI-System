import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load Dataset
df = pd.read_excel(
    r"C:\Users\umesh kavle\OneDrive\Documents\Ecommerce_BI_Project\dataset\Superstore.xlsx"
)

# Monthly Sales
monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

# Month Numbers
monthly_sales["Month_Num"] = range(1, len(monthly_sales) + 1)

X = monthly_sales[["Month_Num"]]
y = monthly_sales["Sales"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predict Next Month
next_month = np.array([[13]])

prediction = model.predict(next_month)

print("=" * 50)
print("SALES FORECAST")
print("=" * 50)
print(f"Predicted Next Month Sales: {prediction[0]:,.2f}")