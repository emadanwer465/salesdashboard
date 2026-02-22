import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

df["Returns"] = np.random.randint(0,3,len(df))

st.title("Sales Dashboard")

st.header("Total Revenue")
st.write(df["Revenue"].sum())

st.header("Sales by Product")

sales_product = df.groupby("Product Category")["Revenue"].sum()

st.bar_chart(sales_product)

st.header("Marketing Impact")

sales_channel = df.groupby("Channel")["Revenue"].sum()

st.bar_chart(sales_channel)

st.header("Seasonal Trends")

sales_month = df.groupby("Month")["Revenue"].sum()

st.line_chart(sales_month)

st.header("Returns")

returns = df.groupby("Product Category")["Returns"].sum()

st.bar_chart(returns)