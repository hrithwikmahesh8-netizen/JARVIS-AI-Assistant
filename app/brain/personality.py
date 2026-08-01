import datetime
import random



def greeting():

    hour = datetime.datetime.now().hour


    if hour < 12:

        return "Good morning, Hrithwik."


    elif hour < 17:

        return "Good afternoon, Hrithwik."


    elif hour < 21:

        return "Good evening, Hrithwik."


    else:

        return "Good night, Hrithwik."




def response(data):

    category = data[0]

    action = data[1]



    replies = {



        "open": [

            f"Certainly Hrithwik, opening {action}.",

            f"Right away, opening {action}.",

            f"Opening {action} for you."

        ],



        "close": [

            f"Closing {action}, Hrithwik.",

            f"{action} has been closed.",

            f"Done. {action} is now closed."

        ],



        "error": [

            "I couldn't complete that task.",

            "I ran into a problem while doing that.",

            "Unable to complete the request."

        ]

    }



    if category in replies:


        return random.choice(
            replies[category]
        )



    return "Done, Hrithwik."