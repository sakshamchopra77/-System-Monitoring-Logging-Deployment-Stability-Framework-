# 🚀 System Monitoring, Logging & Deployment Stability Framework

A production-ready backend system built using FastAPI that monitors system performance, logs activity, and triggers alerts based on resource usage. The project is fully containerized using Docker for easy deployment.

---

## 📌 Features

- 🔍 Real-time CPU monitoring
- 🧠 Memory usage tracking
- 📝 Logging system (info & error logs)
- 🚨 Alert system for high resource usage
- ⚡ FastAPI-based backend
- 🐳 Docker & Docker Compose support

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Psutil
- Docker
- Docker Compose

---

## 📂 Project Structure
.
├── app.py
├── monitor.py
├── logger.py
├── alerts.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore


---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload

OPEN
http://127.0.0.1:8000

RUN WITH DOCKER
docker build -t ai-monitoring .
docker run -p 8000:8000 ai-monitoring

RUN WITH DOCKER COMPOSE
docker compose up --build
OPEN
http://localhost:8000

🔍 API Endpoints
Endpoint	Description
/	Welcome message
/health	Health check
/metrics	CPU & Memory usage
/logs	View application logs

⚠️ Alert Conditions

CPU usage > 80%

Memory usage > 80%
