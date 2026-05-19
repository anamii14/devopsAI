from ai_part import generate_ai_report
from graph_visualizer import generate_graph

import json
from collections import defaultdict


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

    for log in logs:
        key = log["service"] + " | " + log["message"]
        log_map[key] = log

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
        elif level == "WARNING":
            severity = "LOW"
        elif level == "INFO":
            severity = "INFO"
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


# ---------------- MENU ----------------

def show_menu():
    print("\n================ DEVOPS AI MENU ================\n")
    print("1. Full Report (AI + Timeline + Incidents + Graph)")
    print("2. Timeline Only")
    print("3. Incident Summary Only")
    print("4. AI Report Only")
    print("5. Graph Only")
    print("6. Exit")
    print("\n===============================================\n")


def main():

    logs = read_logs("logs.txt")
    freq = deduplicate(logs)
    incidents = create_incidents(freq, logs)
    timeline = generate_timeline(logs)

    ai_report = None

    while True:

        show_menu()
        choice = input("Enter choice: ")

        # EXIT
        if choice == "6":
            print("Exiting...")
            break

        # FULL PIPELINE
        if choice == "1":
            print("\n================ TIMELINE ================\n")
            for t in timeline:
                print(t)

            print("\n================ INCIDENTS ================\n")
            for i in incidents:
                print(i)

            print("\n================ AI REPORT ================\n")
            ai_report = generate_ai_report(incidents, timeline, "FULL")
            print(ai_report)

            generate_graph(incidents)

        elif choice == "2":
            print("\n================ TIMELINE ================\n")
            for t in timeline:
                print(t)

        elif choice == "3":
            print("\n================ INCIDENTS ================\n")
            for i in incidents:
                print(i)

        elif choice == "4":
            print("\n================ AI REPORT ================\n")
            ai_report = generate_ai_report(incidents, timeline, "FULL")
            print(ai_report)

        elif choice == "5":
            generate_graph(incidents)

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()