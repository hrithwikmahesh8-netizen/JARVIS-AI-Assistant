import requests


def ask_ai(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": f"""
You are JARVIS, a helpful personal AI assistant.
Answer clearly and briefly.

User: {prompt}
JARVIS:
""",
            "stream": False
        }
    )

    result = response.json()

    return result["response"]