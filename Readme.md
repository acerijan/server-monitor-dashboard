# Linux Server Monitoring Dashboard

## Overview
A lightweight DevOps-style monitoring dashboard built using Python and Streamlit to visualize real-time system metrics.

## Features
- CPU usage monitoring
- RAM usage tracking
- Disk usage visualization
- System information display
- Dockerized deployment

## Tech Stack
- Python
- Streamlit
- psutil
- Docker
- Linux

## How to Run

### Without Docker
```bash
pip install -r requirements.txt
streamlit run app.py
```

### With Docker
```bash
docker build -t server-monitor .
docker run -p 8501:8501 server-monitor