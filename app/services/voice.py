import sounddevice as sd
import soundfile as sf
import speech_recognition as sr


def listen():

    filename = "input.wav"

    print("Listening...")

    recording = sd.rec(
        int(5 * 44100),
        samplerate=44100,
        channels=1
    )

    sd.wait()

    sf.write(
        filename,
        recording,
        44100
    )

    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except Exception:
        return ""