import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_ai_report(incidents, timeline, mode="FULL"):

    if not API_KEY:
        return "ERROR: OPENROUTER_API_KEY not found in environment variables"

    base_rules = """
You are a Senior Site Reliability Engineer (SRE) in a DevOps team.

Rules:
- Use bullet points only
- Be concise and technical
- No emojis
- No raw log repetition
- Follow mode strictly
"""

    mode_instructions = {
        "FULL": """
Return:
1. Incident Summary
2. Root Cause Analysis
3. Impact Analysis
4. Recommended Fixes
Include cascading failures and dependency chain.
""",

        "SUMMARY": """
Return ONLY Incident Summary.
""",

        "ROOT_CAUSE": """
Return ONLY Root Cause Analysis.
Focus on trigger event and cascading failures.
""",

        "IMPACT": """
Return ONLY Impact Analysis.
""",

        "FIXES": """
Return ONLY Recommended Fixes (engineering actions only).
"""
    }

    prompt = f"""
{base_rules}

DATA:

INCIDENTS:
{json.dumps(incidents, indent=2)}

TIMELINE:
{timeline}

TASK:
{mode_instructions.get(mode, mode_instructions["FULL"])}
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

        if response.status_code != 200:
            return f"HTTP ERROR {response.status_code}: {result}"

        if "choices" not in result:
            return f"API ERROR RESPONSE: {result}"

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERROR: AI request failed - {str(e)}"