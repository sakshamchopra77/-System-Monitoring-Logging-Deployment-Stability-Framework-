from fastapi import FastAPI
import time
import threading

from monitor import get_system_metrics
from logger import log_info, log_error
from alerts import send_alert

app = FastAPI()

def monitoring_loop():
    while True:
        metrics = get_system_metrics()

        cpu = metrics["cpu_usage"]
        memory = metrics["memory_usage"]

        log_info(f"CPU: {cpu}%, Memory: {memory}%")

        if cpu > 80:
            log_error("High CPU Usage")
            send_alert("CPU usage exceeded 80%")

        if memory > 80:
            log_error("High Memory Usage")
            send_alert("Memory usage exceeded 80%")

        time.sleep(10)

thread = threading.Thread(target=monitoring_loop)
thread.daemon = True
thread.start()

@app.get("/")
def home():
    return {"message": "AI Monitoring Running"}

@app.get("/health")
def health():
    return {"status": "running"}

@app.get("/metrics")
def metrics():
    return get_system_metrics()