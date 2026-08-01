import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import tempfile
import os



def listen():

    print("Listening...")


    sample_rate = 16000
    seconds = 5


    filename = tempfile.mktemp(
        suffix=".wav"
    )


    audio_data = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )


    sd.wait()


    wav.write(
        filename,
        sample_rate,
        audio_data
    )


    recognizer = sr.Recognizer()


    try:

        with sr.AudioFile(filename) as source:

            audio = recognizer.record(source)


        text = recognizer.recognize_google(
            audio
        )


        os.remove(filename)


        return text



    except sr.UnknownValueError:

        os.remove(filename)

        return ""



    except Exception as e:

        print(
            "LISTEN ERROR:",
            e
        )

        if os.path.exists(filename):

            os.remove(filename)

        return ""