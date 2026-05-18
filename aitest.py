import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "DevOps Incident Test"
    },
    json={
        "model": "meta-llama/llama-3.1-70b-instruct",
        "messages": [
            {
                "role": "user",
                "content": "Explain what a DevOps incident is in 2 lines."
            }
        ]
    }
)

print(response.json()["choices"][0]["message"]["content"])