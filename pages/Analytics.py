import streamlit as st
from analytics.anomaly_detection import detect_anomalies

st.title("🤖 Network Analytics")

anomalies = detect_anomalies()

if anomalies.empty:
    st.success("No anomalies detected")
else:
    st.error(f"{len(anomalies)} anomalies detected")
    st.dataframe(anomalies)