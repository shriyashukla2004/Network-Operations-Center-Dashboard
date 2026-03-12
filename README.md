#📡 AI-Powered Network Operations Center (NOC) Dashboard

A real-time network monitoring and analytics platform designed to simulate a telecom-style Network Operations Center (NOC).
The system collects network telemetry, detects anomalies using machine learning, and visualizes network health through an interactive Streamlit dashboard.

This project demonstrates concepts used in telecom monitoring systems, infrastructure analytics, and network automation platforms.

🚀 Features
📊 Real-Time Network Monitoring

Device status tracking (UP/DOWN)

Latency monitoring across network nodes

Automated data collection pipeline

🧠 AI-Based Network Analytics

Anomaly detection using Isolation Forest

Identifies abnormal latency spikes

Early detection of potential network failures

📡 Network Topology Visualization

Interactive topology graph using NetworkX + PyVis

Visual representation of network infrastructure

📈 Advanced Data Visualization

Latency trend analysis using Plotly

Network latency heatmap analytics

Device performance metrics

🚨 Alert System

Detects abnormal network behavior

Displays real-time alerts in the NOC dashboard

📜 Network Logs

Historical telemetry storage using SQLite

Log inspection for network troubleshooting

🔄 Real-Time Dashboard

Auto-refresh monitoring every few seconds

NOC-style monitoring interface built with Streamlit

🏗 System Architecture

The platform follows a network telemetry pipeline architecture similar to enterprise monitoring systems.

Network Devices
      │
      ▼
Monitoring Agent (Python Ping Telemetry)
      │
      ▼
SQLite Database
      │
      ▼
Analytics Engine
  ├── Anomaly Detection
  ├── Latency Analysis
  └── Network Metrics
      │
      ▼
Streamlit NOC Dashboard
📂 Project Structure
network-noc-dashboard

app.py                     # Main application entry point

pages/
   1_Dashboard.py          # Monitoring dashboard
   2_Topology.py           # Network topology visualization
   3_Analytics.py          # AI anomaly detection
   4_Logs.py               # Network logs viewer

analytics/
   __init__.py
   anomaly_detection.py    # ML-based anomaly detection

data/
   network_logs.db         # Network telemetry database

topology.py                # Network topology builder

requirements.txt           # Project dependencies
🛠 Tech Stack
Category	Technologies
Dashboard	Streamlit
Visualization	Plotly, PyVis
Graph Modeling	NetworkX
Data Processing	Pandas
Database	SQLite
Machine Learning	Scikit-learn
Networking	Python ICMP telemetry
⚙ Installation

Clone the repository:

git clone https://github.com/yourusername/network-noc-dashboard.git
cd network-noc-dashboard

Create virtual environment:

python -m venv .venv

Activate environment:

Windows

.venv\Scripts\activate

Mac/Linux

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt
▶ Running the Dashboard

Start the Streamlit application:

streamlit run app.py

The dashboard will be available at:

http://localhost:8501
📊 Dashboard Overview

The NOC dashboard provides:

Network device health monitoring

Latency trend visualization

Network topology map

AI anomaly alerts

Network heatmap analytics

Historical telemetry logs

🧠 Machine Learning Component

The system uses Isolation Forest for anomaly detection.

The model identifies unusual latency patterns that may indicate:

network congestion

routing issues

packet loss

infrastructure instability

This approach mimics real-world telemetry anomaly detection used in telecom networks.

📈 Example Use Cases

This platform can simulate monitoring scenarios such as:

ISP infrastructure monitoring

data center network analytics

telecom network performance monitoring

network anomaly detection research

📌 Future Improvements

Potential enhancements include:

Distributed monitoring agents

packet traffic analysis

predictive network failure modeling

cloud deployment

real-time streaming telemetry

role-based access control

🎯 Learning Outcomes

This project demonstrates practical knowledge of:

network monitoring systems

infrastructure analytics

anomaly detection in telemetry data

data visualization for network operations

real-time dashboard development

👩‍💻 Author

Shriya Shukla

B.Tech – Computer Science
Data Analytics & Machine Learning Enthusiast
