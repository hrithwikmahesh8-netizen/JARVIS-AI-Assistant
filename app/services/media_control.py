import pyautogui
import pywhatkit



def media_command(command):

    command = command.lower().strip()




    # =========================
    # PLAY YOUTUBE MUSIC
    # =========================

    if command.startswith("play"):


        song = command.replace(

            "play",

            "",

            1

        ).strip()



        if song:


            pywhatkit.playonyt(song)



            return (

                f"Playing {song} on YouTube."

            )





    # =========================
    # PAUSE
    # =========================

    if "pause" in command:


        pyautogui.press(

            "playpause"

        )


        return "Pausing music."





    # =========================
    # RESUME
    # =========================

    if (

        "resume" in command

        or

        "continue music" in command

    ):


        pyautogui.press(

            "playpause"

        )


        return "Resuming music."





    # =========================
    # NEXT SONG
    # =========================

    if (

        "next song" in command

        or

        "next track" in command

    ):


        pyautogui.press(

            "nexttrack"

        )


        return "Playing next song."





    # =========================
    # PREVIOUS SONG
    # =========================

    if (

        "previous song" in command

        or

        "previous track" in command

    ):


        pyautogui.press(

            "prevtrack"

        )


        return "Playing previous song."





    # =========================
    # VOLUME CONTROL
    # =========================

    if "volume up" in command:


        pyautogui.press(

            "volumeup",

            presses=3

        )


        return "Increasing volume."





    if "volume down" in command:


        pyautogui.press(

            "volumedown",

            presses=3

        )


        return "Decreasing volume."





    if "mute" in command:


        pyautogui.press(

            "volumemute"

        )


        return "Muting volume."





    return None