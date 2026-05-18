import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_ai_report(incidents, timeline):
    if not API_KEY:
        return "ERROR: OPENROUTER_API_KEY not found in environment variables"

    prompt = f"""
You are a Senior Site Reliability Engineer (SRE) in a DevOps team.

You are analyzing system incidents from logs.

Your job is to produce a structured professional incident report.

DATA:

INCIDENTS:
{json.dumps(incidents, indent=2)}

TIMELINE:
{timeline}

TASK:

Generate a clear incident report with:

1. Incident Summary (what happened)
2. Root Cause Analysis (why it likely happened)
3. Impact Analysis (what systems/users affected)
4. Recommended Fixes (engineering actions)

Also identify:
- cascading failures
- service dependency chain
- likely root trigger event
- whether this is symptom vs root cause


Rules:
- reduce unnecessary symbols and headings
- Points rather than paragraphs
- Be concise and dont be repetitive
- Be precise and technical
- Do NOT repeat raw logs
- Infer relationships between incidents
- Group related failures logically
- No emojis
- Keep it production-grade (like Datadog report)
"""

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "AI DevOps Incident System"
            },
            json={
                "model": "meta-llama/llama-3.1-70b-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.2
            },
            timeout=30
        )

        result = response.json()

        # safer extraction
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERROR: AI request failed - {str(e)}"