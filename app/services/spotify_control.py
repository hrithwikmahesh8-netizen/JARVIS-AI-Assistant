import webbrowser
import urllib.parse
import subprocess
import time



def open_spotify():

    try:

        subprocess.Popen(

            "start spotify:",

            shell=True

        )


        time.sleep(5)


        return True



    except:


        return False





def spotify_command(command):

    command = command.lower().strip()




    # =========================
    # OPEN SPOTIFY
    # =========================

    if "open spotify" in command:


        if open_spotify():


            return "Opening Spotify."



        return "Unable to open Spotify."





    # =========================
    # PLAY SONG ON SPOTIFY
    # =========================

    if (

        "spotify" in command

        and

        "play" in command

    ):


        song = command.replace(

            "play",

            "",

            1

        )



        song = song.replace(

            "on spotify",

            ""

        )



        song = song.replace(

            "in spotify",

            ""

        )



        song = song.replace(

            "spotify",

            ""

        )



        song = song.strip()





        if song:


            open_spotify()


            time.sleep(3)



            url = (

                "https://open.spotify.com/search/"

                +

                urllib.parse.quote(song)

            )



            webbrowser.open(url)



            return (

                f"Searching {song} on Spotify."

            )





    # =========================
    # PAUSE SPOTIFY
    # =========================

    if "pause spotify" in command:


        import pyautogui


        pyautogui.press(

            "playpause"

        )


        return "Pausing Spotify."





    # =========================
    # NEXT SONG
    # =========================

    if (

        "next song" in command

        or

        "skip song" in command

    ):


        import pyautogui


        pyautogui.press(

            "nexttrack"

        )


        return "Skipping song."





    return None