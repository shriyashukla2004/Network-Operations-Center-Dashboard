from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

os.makedirs("data", exist_ok=True)

def save_data(data):

    conn = sqlite3.connect("data/network_logs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS network_logs (
    timestamp TEXT,
    device TEXT,
    latency REAL,
    status TEXT,
    agent TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO network_logs VALUES (?, ?, ?, ?, ?)",
        (
            data["timestamp"],
            data["device"],
            data["latency"],
            data["status"],
            data["agent"]
        )
    )

    conn.commit()
    conn.close()


@app.route("/log", methods=["POST"])
def log():

    data = request.json
    save_data(data)

    return {"message": "data stored"}, 200


if __name__ == "__main__":
    app.run(port=5000)