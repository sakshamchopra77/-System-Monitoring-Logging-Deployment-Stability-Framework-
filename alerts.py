def send_alert(message):
    with open("alerts.log", "a") as f:
        f.write(f"ALERT: {message}\n")