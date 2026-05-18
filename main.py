import json
from collections import defaultdict
from ai_part import generate_ai_report
from graph_visualizer import generate_graph

import os
import matplotlib.pyplot as plt


# 1. Read JSON logs
def read_logs(file_path):
    logs = []

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()

            if not line:
                continue

            try:
                logs.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"[LINE {i}] Invalid JSON → {line}")

    return logs

# 2. Deduplicate
def deduplicate(logs):
    freq = defaultdict(int)

    for log in logs:
        key = log["service"] + " | " + log["message"]
        freq[key] += 1

    return freq


# 3. Create incidents
def create_incidents(freq, logs):
    incidents = []

    log_map = {}
    for log in logs:
        key = log["service"] + " | " + log["message"]
        log_map[key] = log  # keep full context

    for issue, count in freq.items():
        service, message = issue.split(" | ")
        base_log = log_map.get(issue)

        level = base_log["level"] if base_log else ""
        timestamp = base_log["timestamp"] if base_log else None

        if level == "CRITICAL":
            severity = "CRITICAL"
        elif level == "ERROR" and count > 1:
            severity = "HIGH"
        elif level == "ERROR":
            severity = "MEDIUM"
        else:
            severity = "LOW"

        incidents.append({
            "service": service,
            "issue": message,
            "count": count,
            "severity": severity,
            "level": level,
            "timestamp": timestamp   
        })

    return incidents


# 4. Timeline
def generate_timeline(logs):
    return [
        f"{log['timestamp']} | {log['level']} | {log['service']} | {log['message']}"
        for log in logs
    ]


# 5. MAIN PIPELINE
def main():
    logs = read_logs("logs.txt")

    freq = deduplicate(logs)
    incidents = create_incidents(freq, logs)
    timeline = generate_timeline(logs)

    

    print("\n================ TIMELINE ================\n")
    for t in timeline:
        print(t)

    print("\n================ AI REPORT ================\n")

    try:
       report = generate_ai_report(incidents, timeline)

       with open("ai_report.txt", "w", encoding="utf-8") as f:
        f.write(str(report))

       print("AI report saved to ai_report.txt")
    except Exception as e:
        print("AI REPORT FAILED:", str(e))

    generate_graph(incidents)    
    

if __name__ == "__main__":
    main()