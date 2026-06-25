import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from pathlib import Path

# Page Config
st.set_page_config(page_title="E-Commerce BI Dashboard")

st.title("🛒 E-Commerce Business Intelligence Dashboard")

# Load Data (Works on Local + Streamlit Cloud)
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "dataset" / "Superstore.xlsx"

df = pd.read_excel(file_path)

# Sidebar Filters
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

segment = st.sidebar.multiselect(
    "Select Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

# Apply Filters
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment))
]

# KPI Metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

profit_margin = (total_profit / total_sales) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{total_sales:,.0f}")
col2.metric("Total Profit", f"{total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Profit Margin", f"{profit_margin:.2f}%")

st.markdown("---")

# Monthly Sales
st.subheader("Monthly Sales")

monthly_sales = filtered_df.groupby("Month")["Sales"].sum()

fig, ax = plt.subplots(figsize=(10, 5))
monthly_sales.plot(kind="bar", ax=ax)

ax.set_title("Monthly Sales")
ax.set_ylabel("Sales")

st.pyplot(fig)

# Top Customers
st.subheader("Top 10 Customers")

top_customers = (
    filtered_df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_customers)

# Top States
st.subheader("Top 10 States")

top_states = (
    filtered_df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_states)

# Top Products
st.subheader("Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# Download CSV
st.markdown("---")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)

# Forecast
st.markdown("---")
st.subheader("📈 Sales Forecast")

forecast_data = (
    filtered_df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

forecast_data["Month_Num"] = range(
    1,
    len(forecast_data) + 1
)

X = forecast_data[["Month_Num"]]
y = forecast_data["Sales"]

model = LinearRegression()
model.fit(X, y)

next_month = np.array([[len(forecast_data) + 1]])

prediction = model.predict(next_month)

st.metric(
    "Predicted Next Month Sales",
    f"{prediction[0]:,.0f}"
)

# Forecast Graph
st.subheader("📈 Sales Forecast Trend")

forecast_months = list(range(1, len(forecast_data) + 1))
forecast_sales = list(y)

forecast_months.append(len(forecast_data) + 1)
forecast_sales.append(prediction[0])

forecast_df = pd.DataFrame({
    "Month": forecast_months,
    "Sales": forecast_sales
})

st.line_chart(
    forecast_df.set_index("Month")
)