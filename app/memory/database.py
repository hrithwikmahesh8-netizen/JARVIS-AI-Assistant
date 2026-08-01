import json
import os


MEMORY_FILE = "app/memory/memories.json"

CHAT_FILE = "app/memory/chat_history.json"



def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {}


    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as file:

            return json.load(file)


    except:

        return {}



def save_memory(memory):

    os.makedirs(
        "app/memory",
        exist_ok=True
    )


    with open(
        MEMORY_FILE,
        "w"
    ) as file:


        json.dump(
            memory,
            file,
            indent=4
        )



def remember(key, value):

    memory = load_memory()


    memory[key] = value


    save_memory(
        memory
    )



def recall(key):

    memory = load_memory()


    return memory.get(
        key
    )



def all_memories():

    return load_memory()



def add_chat(user, assistant):

    os.makedirs(
        "app/memory",
        exist_ok=True
    )


    history = []


    if os.path.exists(CHAT_FILE):

        try:

            with open(
                CHAT_FILE,
                "r"
            ) as file:

                history = json.load(file)


        except:

            history = []



    history.append(

        {
            "user": user,
            "assistant": assistant
        }

    )



    with open(
        CHAT_FILE,
        "w"
    ) as file:


        json.dump(
            history,
            file,
            indent=4
        )