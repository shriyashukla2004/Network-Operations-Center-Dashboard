import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.title("📊 Network Dashboard")

conn = sqlite3.connect("data/network_logs.db")
df = pd.read_sql("SELECT * FROM network_logs", conn)
conn.close()

df["timestamp"] = pd.to_datetime(df["timestamp"])

devices = df["device"].unique()

col1, col2, col3 = st.columns(3)

col1.metric("Devices", len(devices))
col2.metric("Failures", (df["status"]=="DOWN").sum())
col3.metric("Avg Latency", round(df["latency"].mean(),3))

device = st.selectbox("Select Device", devices)

device_df = df[df["device"]==device]

fig = px.line(device_df, x="timestamp", y="latency", markers=True)

st.plotly_chart(fig, use_container_width=True)