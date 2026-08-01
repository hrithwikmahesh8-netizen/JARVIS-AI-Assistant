import os
import datetime
import subprocess


from app.services.app_finder import find_app
from app.services.process_control import close_process
from app.services.power_control import power_command
from app.services.system_monitor import monitor_command
from app.services.browser_control import browser_command
from app.services.media_control import media_command
from app.services.spotify_control import spotify_command


from app.brain.personality import response




def system_command(command):

    command = command.lower().strip()



    # =========================
    # SPOTIFY
    # =========================

    result = spotify_command(command)


    if result:

        return result




    # =========================
    # MEDIA
    # =========================

    result = media_command(command)


    if result:

        return result




    # =========================
    # BROWSER
    # =========================

    result = browser_command(command)


    if result:

        return result




    # =========================
    # POWER
    # =========================

    result = power_command(command)


    if result:

        return result




    # =========================
    # SYSTEM MONITOR
    # =========================

    result = monitor_command(command)


    if result:

        return result




    # =========================
    # TIME
    # =========================

    if "time" in command:


        now = datetime.datetime.now()


        return (

            f"The current time is "
            f"{now.strftime('%I:%M %p')}."

        )




    # =========================
    # DATE
    # =========================

    if (

        "date" in command

        or

        "today" in command

        or

        "day" in command

    ):


        now = datetime.datetime.now()


        return (

            f"Today is "
            f"{now.strftime('%A, %d %B %Y')}."

        )




    # =========================
    # RECYCLE BIN
    # =========================

    if (

        "recycle bin" in command

        or

        "recyclebin" in command

        or

        "trash" in command

    ):


        try:


            subprocess.Popen(

                [

                    "explorer.exe",

                    "shell:RecycleBinFolder"

                ]

            )


            return "Opening recycle bin."



        except:


            return "Unable to open recycle bin."





    # =========================
    # MICROSOFT EDGE
    # =========================

    if (

        "open edge" in command

        or

        "open microsoft edge" in command

    ):


        edge_paths = [


            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",


            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

        ]



        for path in edge_paths:


            if os.path.exists(path):


                os.startfile(path)


                return response(

                    ("open", "Microsoft Edge")

                )



        return "Unable to open Microsoft Edge."





    # =========================
    # CLOSE APPLICATION
    # =========================

    if command.startswith("close"):


        app = command.replace(

            "close",

            "",

            1

        ).strip()



        result = close_process(app)



        if result:


            return response(

                ("close", app)

            )



        return f"{app} is not running."





    # =========================
    # OPEN APPLICATION
    # =========================

    if command.startswith("open"):


        app = command.replace(

            "open",

            "",

            1

        ).strip()



        path = find_app(app)



        if path:


            try:


                os.startfile(path)



                return response(

                    ("open", app)

                )



            except:


                return (

                    "Unable to open "

                    + app

                )




        return (

            "I could not find "

            + app

        )





    return None