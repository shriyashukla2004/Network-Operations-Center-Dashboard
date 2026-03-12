import pandas as pd
import sqlite3
from sklearn.ensemble import IsolationForest

def detect_anomalies():

    conn = sqlite3.connect("data/network_logs.db")

    df = pd.read_sql("SELECT * FROM network_logs", conn)

    conn.close()

    # remove failed pings
    df = df[df["latency"] > 0]

    model = IsolationForest(contamination=0.05)

    df["anomaly"] = model.fit_predict(df[["latency"]])

    anomalies = df[df["anomaly"] == -1]

    return anomalies