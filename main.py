import time

from app.brain.assistant import ask_ai
from app.voice.wake_word import wait_for_jarvis
from app.voice.listen import listen
from app.voice.speak import speak


def startup():
    message = "Hello Hrithwik. JARVIS AI is online."
    print("JARVIS:", message)
    speak(message)


def main():

    startup()

    while True:

        try:
            # Wait for wake word
            wait_for_jarvis()

            print("JARVIS activated.")
            speak("Yes Hrithwik?")

            # Listen for user command
            command = listen()

            if not command:
                continue

            command = command.strip()

            print("You:", command)

            # Shutdown commands
            if command.lower() in [
                "stop jarvis",
                "shutdown jarvis",
                "exit jarvis",
                "goodbye jarvis",
                "bye jarvis",
                "go offline"
            ]:

                print("JARVIS: Going offline.")
                speak("Going offline.")
                break

            # Process command
            answer = ask_ai(command)

            if answer:
                print("JARVIS:", answer)
                speak(answer)

        except KeyboardInterrupt:

            print("\nJARVIS stopped.")
            speak("Goodbye Hrithwik.")
            break

        except Exception as e:

            print("JARVIS ERROR:", e)

            time.sleep(1)


if __name__ == "__main__":
    main()