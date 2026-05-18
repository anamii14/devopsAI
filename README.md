Here’s your **updated and improved version** (clean, more professional, includes report logging + graph generation, and still concise):

---

# # devopsAI

AI-Powered DevOps Incident Analysis System

---

## Project Description

This project is an AI-assisted DevOps monitoring and incident analysis system that processes structured system logs, detects incidents, and generates automated incident reports using a large language model via OpenRouter API.

It simulates modern observability platforms by combining log processing, incident grouping, timeline reconstruction, AI-driven root cause analysis, report logging, and incident graph generation for visualization.

---

## How It Works

### Log Ingestion

Reads structured JSON logs containing timestamp, service, log level, and message.

---

### Log Processing

* Deduplicates repeated log events
* Groups logs by service and message

---

### Incident Generation

* Converts grouped logs into incidents
* Assigns severity levels based on log level and frequency

---

### Timeline Reconstruction

Builds a chronological view of system events.

---

### AI Analysis Layer

Sends incidents and timeline to a large language model via OpenRouter and generates:

* Incident Summary
* Root Cause Analysis
* Impact Analysis
* Recommended Fixes

---

### Reporting & Visualization

* Logs and stores AI-generated incident reports for tracking
* Generates incident graphs for visual analysis

---

## Key Features

* JSON-based structured log processing
* Incident detection and grouping
* Severity classification (LOW / MEDIUM / HIGH / CRITICAL)
* Timeline reconstruction of system events
* AI-powered incident report generation
* Report logging and storage
* Incident graph generation for visualization
* Secure API key handling using `.env`
* Modular Python architecture

---

## Tech Stack

* Python
* OpenRouter API (LLM integration)
* JSON log processing
* Matplotlib (graph generation)
* python-dotenv

---

## Example Use Case

The system analyzes logs such as:

* Database failures
* API latency spikes
* Service outages
* System warnings and critical errors

It converts them into structured incident reports and visual graphs similar to those used in DevOps monitoring platforms.

---

## Purpose

This project demonstrates how AI can enhance DevOps workflows by:

* Reducing manual log analysis
* Grouping related system failures
* Generating automated incident reports
* Storing reports for audit/history
* Visualizing incidents using graphs
* Assisting in root cause analysis

It serves as a simplified AIOps-style observability and incident management system inspired by real-world production tools.
