import requests
import json

from app.memory.database import remember, recall, add_chat
from app.services.system_control import system_command


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
    # PC CONTROL COMMANDS
    # --------------------------------

    system_response = system_command(command)

    if system_response:
        add_chat(original_prompt, system_response)
        return system_response



    # --------------------------------
    # MEMORY RECALL
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
    # AUTOMATIC LEARNING
    # --------------------------------


    # Learn name

    if "my name is" in command:

        name = command.replace("my name is", "").strip()

        remember("name", name)

        return f"Nice to meet you {name}. I will remember your name."



    # Learn likes

    if "i like" in command:

        item = command.replace("i like", "").strip()

        remember("like " + item, True)

        return f"I will remember that you like {item}."



    # Learn dislikes

    if "i don't like" in command or "i dislike" in command:

        item = command.replace("i don't like", "")
        item = item.replace("i dislike", "").strip()

        remember("dislike " + item, True)

        return f"I will remember that you don't like {item}."



    # --------------------------------
    # LOCAL AI RESPONSE
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
- You are NOT Tony Stark's JARVIS.
- Do not mention Marvel or Tony Stark.
- Never invent information about Hrithwik.
- Only use information provided by Hrithwik.
- If you don't know something, say you don't know.
- Be helpful and concise.

User:
{original_prompt}

JARVIS:
""",

            "stream": False
        }
    )


    answer = response.json()["response"]


    # Save conversation

    add_chat(original_prompt, answer)


    return answer