from ping3 import ping
from datetime import datetime
import sqlite3
from devices import devices
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/network_logs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS network_logs (
timestamp TEXT,
device TEXT,
latency REAL,
status TEXT
)
""")

for device in devices:

    latency = ping(device)

    if latency is None:
        status = "DOWN"
        latency = -1
    else:
        status = "UP"

    timestamp = datetime.now()

    cursor.execute(
        "INSERT INTO network_logs VALUES (?, ?, ?, ?)",
        (timestamp, device, latency, status)
    )

conn.commit()
conn.close()