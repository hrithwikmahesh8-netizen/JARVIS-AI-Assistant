import json
import requests

from app.memory.database import (
    add_chat,
    remember,
    recall
)

from app.memory.memory_manager import process_memory

from app.services.system_control import system_command



def load_profile():

    try:

        with open(
            "app/memory/user_profile.json",
            "r"
        ) as file:

            return json.load(file)

    except:

        return {}



def ask_ai(prompt):

    original_prompt = prompt.strip()

    command = original_prompt.lower()



    # =========================
    # SYSTEM COMMANDS
    # =========================

    system_response = system_command(
        original_prompt
    )


    if system_response:

        add_chat(
            original_prompt,
            system_response
        )

        return system_response



    # =========================
    # MEMORY SYSTEM
    # =========================

    memory_response = process_memory(
        original_prompt
    )


    if memory_response:

        add_chat(
            original_prompt,
            memory_response
        )

        return memory_response



    # =========================
    # REMEMBER NAME
    # =========================

    if "remember my name is" in command:


        name = (
            original_prompt
            .replace(
                "remember my name is",
                ""
            )
            .strip()
        )


        remember(
            "name",
            name
        )


        answer = (
            f"I will remember your name is {name}."
        )


        add_chat(
            original_prompt,
            answer
        )


        return answer



    # =========================
    # ASK NAME
    # =========================

    if "what is my name" in command:


        name = recall(
            "name"
        )


        if name:

            answer = (
                f"Your name is {name}, Hrithwik."
            )

        else:

            answer = (
                "I don't know your name yet."
            )


        add_chat(
            original_prompt,
            answer
        )


        return answer



    # =========================
    # OLLAMA AI
    # =========================

    profile = load_profile()



    try:

        response = requests.post(

            "http://localhost:11434/api/generate",

            json={

                "model": "llama3.2",

                "prompt": f"""

You are JARVIS, Hrithwik's personal AI assistant.

Personality:
- Intelligent
- Polite
- Helpful
- Futuristic
- Professional


User information:

{profile}


Answer naturally and briefly.


User:
{original_prompt}


JARVIS:

""",

                "stream": False

            }

        )


        answer = (
            response
            .json()
            ["response"]
            .strip()
        )


    except Exception:


        answer = (
            "I am unable to connect to my AI system right now."
        )



    add_chat(
        original_prompt,
        answer
    )


    return answer