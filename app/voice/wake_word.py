import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import tempfile
import os



def wait_for_jarvis():

    recognizer = sr.Recognizer()


    while True:

        print(
            "Waiting for JARVIS wake word..."
        )


        samplerate = 16000
        duration = 4


        filename = tempfile.mktemp(
            suffix=".wav"
        )


        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )


        sd.wait()


        wav.write(
            filename,
            samplerate,
            recording
        )


        try:

            with sr.AudioFile(filename) as source:

                audio = recognizer.record(
                    source
                )


            text = recognizer.recognize_google(
                audio
            ).lower()


            print(
                "Heard:",
                text
            )


            os.remove(filename)



            if (
                "jarvis" in text
                or "hey jarvis" in text
            ):

                return True



        except:

            if os.path.exists(filename):

                os.remove(filename)

            pass