import requests
import json
from app.memory.database import remember, recall, add_chat


def load_profile():

    try:
        with open("app/memory/user_profile.json", "r") as file:
            return json.load(file)

    except:
        return {}



def ask_ai(prompt):

    original_prompt = prompt.strip()
    command = prompt.lower().strip()

    profile = load_profile()


    # --------------------------------
    # Recall questions FIRST
    # --------------------------------

    if "what is my name" in command:

        name = recall("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."



    if "do i like" in command:

        item = command.replace("do i like", "").strip()

        if recall("like " + item):

            return f"Yes, you like {item}."

        if recall("dislike " + item):

            return f"No, you don't like {item}."

        return f"I don't know if you like {item} yet."



    # --------------------------------
    # Automatic learning
    # --------------------------------

    if "my name is" in command:

        name = command.replace("my name is", "").strip()

        remember("name", name)

        return f"Nice to meet you {name}. I will remember your name."



    if "i like" in command:

        item = command.replace("i like", "").strip()

        remember("like " + item, True)

        return f"I will remember that you like {item}."



    if "i don't like" in command or "i dislike" in command:

        item = command.replace("i don't like", "")
        item = item.replace("i dislike", "").strip()

        remember("dislike " + item, True)

        return f"I will remember that you don't like {item}."



    # --------------------------------
    # AI response
    # --------------------------------

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": f"""
You are JARVIS, Hrithwik's personal AI assistant.

User profile:
{profile}

Rules:
- You are not Tony Stark's JARVIS.
- Never invent personal information.
- Only use stored information.
- If you don't know, say you don't know.

User:
{original_prompt}

JARVIS:
""",
            "stream": False
        }
    )

    answer = response.json()["response"]

    add_chat(original_prompt, answer)

    return answer