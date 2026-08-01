from app.services.voice import listen
from app.services.speaker import speak


speak("Hello Hrithwik. JARVIS is online.")


while True:

    command = listen()

    if "hello" in command:
        speak("Hello. How can I help you?")

    elif "exit" in command:
        speak("Goodbye.")
        break