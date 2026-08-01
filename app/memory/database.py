import json
import os


# User facts memory
MEMORY_FILE = "memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(data):

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):

    memory = load_memory()

    return memory.get(key, None)



# Conversation memory
CHAT_FILE = "app/memory/conversations.json"


def load_chat():

    if not os.path.exists(CHAT_FILE):
        return []

    with open(CHAT_FILE, "r") as file:
        return json.load(file)


def save_chat(history):

    with open(CHAT_FILE, "w") as file:
        json.dump(history, file, indent=4)


def add_chat(user, jarvis):

    history = load_chat()

    history.append({
        "user": user,
        "jarvis": jarvis
    })

    save_chat(history)