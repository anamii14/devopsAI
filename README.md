Here’s your **cleaned + slightly more concise + Streamlit-updated version** (still structured, but tighter and more modern):

---

# # devopsAI

AI-Powered DevOps Incident Analysis System

---

## Project Description

This project is an AI-assisted DevOps monitoring system with a **Streamlit web interface** that processes structured JSON logs, detects incidents, and generates automated incident reports using an LLM via OpenRouter API.

It simulates modern observability platforms by combining log processing, incident grouping, timeline reconstruction, AI-driven root cause analysis, report logging, and interactive incident graph visualization.

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

Uses OpenRouter LLM to generate:

* Incident Summary
* Root Cause Analysis
* Impact Analysis
* Recommended Fixes

---

### Reporting & Visualization

* Stores AI-generated reports for tracking
* Generates incident graphs for visualization
* Streamlit UI for interactive analysis

---

## Key Features

* Streamlit-based web dashboard
* JSON log processing pipeline
* Incident detection and grouping
* Severity classification (LOW / MEDIUM / HIGH / CRITICAL)
* Timeline reconstruction
* AI-powered incident analysis
* Report logging and storage
* Incident graph visualization
* Secure API key handling via `.env`
* Modular Python architecture

---

## Tech Stack

* Python
* Streamlit (UI)
* OpenRouter API (LLM integration)
* JSON processing
* Matplotlib (graph visualization)
* python-dotenv

---

## Example Use Case

The system analyzes logs such as:

* Database failures
* API latency spikes
* Service outages
* System warnings and critical errors

It converts them into structured incident reports and visual graphs similar to real-world DevOps monitoring tools.

---

## Purpose

This project demonstrates how AI enhances DevOps workflows by:

* Reducing manual log analysis
* Grouping related system failures
* Generating automated incident reports
* Storing reports for audit/history
* Visualizing incidents interactively
* Assisting root cause analysis

It serves as a simplified **AIOps-style observability system** inspired by production-grade DevOps platforms.

