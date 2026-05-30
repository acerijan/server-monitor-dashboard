import streamlit as st
import psutil
import socket
import platform
import time

st.set_page_config(page_title="Server Monitoring Dashboard")

st.title("Linux Server Monitoring Dashboard")

# Metrics
st.metric("CPU Usage", f"{psutil.cpu_percent()}%")
st.metric("RAM Usage", f"{psutil.virtual_memory().percent}%")
st.metric("Disk Usage", f"{psutil.disk_usage('/').percent}%")

# System Information
st.subheader("System Information")

st.write("Hostname:", socket.gethostname())
st.write("IP Address:", socket.gethostbyname(socket.gethostname()))
st.write("Operating System:", platform.system())
st.write("Platform:", platform.platform())

# Uptime
boot_time = psutil.boot_time()
uptime = time.time() - boot_time

st.write("System Uptime:", f"{int(uptime // 3600)} Hours")