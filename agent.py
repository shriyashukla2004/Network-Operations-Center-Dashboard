from ping3 import ping
from datetime import datetime
import requests
from devices import devices

SERVER = "http://127.0.0.1:5000/log"

AGENT_NAME = "agent_1"

for device in devices:

    latency = ping(device)

    if latency is None:
        status = "DOWN"
        latency = -1
    else:
        status = "UP"

    data = {
        "timestamp": str(datetime.now()),
        "device": device,
        "latency": latency,
        "status": status,
        "agent": AGENT_NAME
    }

    requests.post(SERVER, json=data)
    