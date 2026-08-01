from app.services.voice import listen
from app.services.speaker import speak
from app.brain.assistant import ask_ai


speak("Hello Hrithwik. JARVIS AI is online.")


while True:

    command = listen()

    if command == "":
        continue

    if "exit" in command:
        speak("Shutting down JARVIS.")
        break

    answer = ask_ai(command)

    speak(answer)