def check_alert(device, status):
    if status == "DOWN":
        print(f"ALERT: {device} is DOWN")