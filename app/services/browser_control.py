import webbrowser
import urllib.parse



def browser_command(command):

    command = command.lower().strip()




    # =========================
    # PLAY YOUTUBE
    # =========================

    if command.startswith("play"):


        query = command.replace(

            "play",

            "",

            1

        ).strip()



        query = query.replace(

            "on youtube",

            ""

        )



        query = query.replace(

            "youtube",

            ""

        ).strip()



        if query:


            url = (

                "https://www.youtube.com/results?search_query="

                +

                urllib.parse.quote(query)

            )



            webbrowser.open(url)



            return (

                f"Playing {query} on YouTube."

            )





    # =========================
    # OPEN YOUTUBE
    # =========================

    if (

        "open youtube" in command

        or

        command == "youtube"

    ):


        webbrowser.open(

            "https://www.youtube.com"

        )


        return "Opening YouTube."





    # =========================
    # YOUTUBE SEARCH
    # =========================

    if "youtube search" in command:


        query = command.replace(

            "youtube search",

            ""

        ).strip()



        if query:


            url = (

                "https://www.youtube.com/results?search_query="

                +

                urllib.parse.quote(query)

            )



            webbrowser.open(url)



            return (

                f"Searching YouTube for {query}."

            )





    # =========================
    # GOOGLE SEARCH
    # =========================

    if command.startswith("search"):


        query = command.replace(

            "search",

            "",

            1

        ).strip()



        if query:


            url = (

                "https://www.google.com/search?q="

                +

                urllib.parse.quote(query)

            )



            webbrowser.open(url)



            return (

                f"Searching for {query}."

            )





    return None