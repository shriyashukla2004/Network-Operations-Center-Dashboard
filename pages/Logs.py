import streamlit as st
import pandas as pd
import sqlite3

st.title("📜 Network Logs")

conn = sqlite3.connect("data/network_logs.db")
df = pd.read_sql("SELECT * FROM network_logs", conn)
conn.close()

st.dataframe(df.tail(100))