# devopsAI

AI-Powered DevOps Incident Analysis System

---

## Project Description

This project is an AI-assisted DevOps monitoring and incident analysis system that processes structured system logs, detects incidents, and generates automated incident reports using a large language model via OpenRouter API.

It simulates how modern observability platforms work by combining log processing, incident grouping, timeline reconstruction, and AI-driven root cause analysis.

---

## How It Works

### Log Ingestion

Reads structured JSON logs containing timestamp, service, log level, and message.

### Log Processing

* Deduplicates repeated log events
* Groups logs by service and message

### Incident Generation

* Converts grouped logs into incidents
* Assigns severity levels based on log level and frequency

### Timeline Reconstruction

Builds a chronological view of system events

### AI Analysis Layer

Sends incidents and timeline to a large language model via OpenRouter
Generates:

* Incident Summary
* Root Cause Analysis
* Impact Analysis
* Recommended Fixes

---

## Key Features

* JSON-based structured log processing
* Incident detection and grouping
* Severity classification (LOW / MEDIUM / HIGH / CRITICAL)
* Timeline reconstruction of system events
* AI-powered incident report generation
* Secure API key handling using `.env`
* Modular Python architecture

---

## Tech Stack

* Python
* OpenRouter API (LLM integration)
* JSON log processing
* python-dotenv

---

## Example Use Case

The system analyzes logs such as:

* Database failures
* API latency spikes
* Service outages
* System warnings and critical errors

It then converts them into structured incident reports similar to those used in DevOps monitoring platforms.

---

## Purpose

This project demonstrates how AI can enhance DevOps workflows by:

* Reducing manual log analysis
* Grouping related system failures
* Generating automated incident reports
* Assisting in root cause analysis

It serves as a simplified version of real-world observability and incident management systems used in production environments.
