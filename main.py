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


# 2. Deduplicate logs
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

    # Store latest log for each issue
    for log in logs:
        key = log["service"] + " | " + log["message"]
        log_map[key] = log

    for issue, count in freq.items():

        service, message = issue.split(" | ")

        base_log = log_map.get(issue)

        level = base_log["level"] if base_log else ""
        timestamp = base_log["timestamp"] if base_log else None

        # Severity logic
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


# 4. Generate timeline
def generate_timeline(logs):

    timeline = []

    for log in logs:
        timeline.append(
            f"{log['timestamp']} | "
            f"{log['level']} | "
            f"{log['service']} | "
            f"{log['message']}"
        )

    return timeline


# 5. Print organized incidents
def print_incidents(incidents):

    severity_order = {
        "CRITICAL": 4,
        "HIGH": 3,
        "MEDIUM": 2,
        "LOW": 1
    }

    
    sorted_incidents = sorted(
        incidents,
        key=lambda x: severity_order[x["severity"]],
        reverse=True
    )

    print("\n================ INCIDENT SUMMARY ================\n")

    for i, incident in enumerate(sorted_incidents, 1):

        print(f"Incident #{i}")
        print(f"Service     : {incident['service']}")
        print(f"Issue       : {incident['issue']}")
        print(f"Log Level   : {incident['level']}")
        print(f"Severity    : {incident['severity']}")
        print(f"Occurrences : {incident['count']}")
        print(f"Timestamp   : {incident['timestamp']}")

        print("-" * 55)


# 6. MAIN PIPELINE
def main():

    # Read logs
    logs = read_logs("logs.txt")

    # Process logs
    freq = deduplicate(logs)

    incidents = create_incidents(freq, logs)

    timeline = generate_timeline(logs)

    # Print timeline
    print("\n================ TIMELINE ================\n")

    for t in timeline:
        print(t)

    # Print incidents nicely
    print_incidents(incidents)

    # AI Report
    print("\n================ AI REPORT ================\n")

    try:

        report = generate_ai_report(incidents, timeline)

        with open("ai_report.txt", "w", encoding="utf-8") as f:
            f.write(str(report))

        print(report)

        print("\nAI report saved to ai_report.txt")

    except Exception as e:

        print("AI REPORT FAILED:", str(e))

    # Generate graph
    generate_graph(incidents)


# Run program
if __name__ == "__main__":
    main()