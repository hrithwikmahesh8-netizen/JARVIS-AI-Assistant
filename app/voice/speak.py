import asyncio
import os
import tempfile

import edge_tts
import pygame



# JARVIS voice

VOICE = "en-US-GuyNeural"





def speak(text):

    if not text:

        return



    print(

        "SPEAK:",

        text

    )


    try:

        asyncio.run(

            _speak(text)

        )


    except Exception as e:


        print(

            "Speech error:",

            e

        )







async def _speak(text):


    filename = os.path.join(

        tempfile.gettempdir(),

        "jarvis_voice.mp3"

    )



    communicate = edge_tts.Communicate(

        text,

        VOICE

    )



    await communicate.save(

        filename

    )





    pygame.mixer.init()



    pygame.mixer.music.load(

        filename

    )



    pygame.mixer.music.play()




    while pygame.mixer.music.get_busy():


        await asyncio.sleep(

            0.1

        )




    pygame.mixer.quit()



    try:


        os.remove(

            filename

        )


    except:


        pass