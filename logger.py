from datetime import datetime

def log_info(message):
    with open("app.log", "a") as f:
        f.write(f"[INFO] {datetime.now()} - {message}\n")

def log_error(message):
    with open("app.log", "a") as f:
        f.write(f"[ERROR] {datetime.now()} - {message}\n")