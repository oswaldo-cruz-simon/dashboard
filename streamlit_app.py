import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Transaction Analysis", layout="wide")

st.title("Transaction Amounts by Month and Transaction Type")

# Example dataframe
# Replace this with your actual dataframe loading logic
df = pd.read_csv("data.csv")

# Sample data

# Convert month to string if needed
df["month"] = df["month"].astype(str)

# Filter selector
selected_is_three = st.selectbox(
    "Select is_three value",
    options=["All", True, False],
    index=0
)

filtered_df = df.copy()

if selected_is_three != "All":
    filtered_df = filtered_df[
        filtered_df["is_three"] == selected_is_three
    ]

# Aggregate in case there are multiple rows per combination
chart_df = (
    filtered_df
    .groupby(["month", "transaction_type"], as_index=False)["amount"]
    .sum()
)

# Double/grouped bar chart
fig = px.bar(
    chart_df,
    x="month",
    y="amount",
    color="transaction_type",
    barmode="group",
    text_auto=".2f",
    title="Amount by Month and Transaction Type"
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Amount",
    legend_title="Transaction Type",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
