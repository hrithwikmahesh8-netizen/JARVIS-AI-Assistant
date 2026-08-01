from app.memory.database import (
    remember,
    all_memories
)



def process_memory(command):

    command_lower = command.lower().strip()



    # ======================
    # LIKE MEMORY
    # ======================

    if command_lower.startswith("i like"):


        item = command[6:].strip()


        if item:


            remember(

                "like_" + item.lower(),

                item

            )


            return (

                f"I'll remember that you like {item}, Hrithwik."

            )




    # ======================
    # DISLIKE MEMORY
    # ======================

    if command_lower.startswith("i hate"):


        item = command[6:].strip()


        if item:


            remember(

                "hate_" + item.lower(),

                item

            )


            return (

                f"I'll remember that you dislike {item}, Hrithwik."

            )




    # ======================
    # SHOW MEMORY
    # ======================

    if (

        "what do you know about me" in command_lower

        or

        "what do you remember about me" in command_lower

    ):


        memories = all_memories()



        if not memories:


            return (

                "I don't have any memories about you yet."

            )



        response = (

            "Here is what I remember about you:"

        )



        for key, value in memories.items():


            if (

                key.startswith("like_")

                or

                key.startswith("hate_")

                or

                key == "name"

            ):


                response += f"\n- {value}"



        return response




    return None