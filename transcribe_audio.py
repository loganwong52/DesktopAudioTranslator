import speech_recognition as sr
import pyaudio


def live_transcribe():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Set up the microphone or virtual audio device
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)

        print("Listening...")

        while True:
            try:
                # Capture audio from the microphone
                audio = recognizer.listen(source)

                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio)

                # Print the recognized text
                print(f"Transcription: {text}")

            except sr.UnknownValueError:
                # In case the speech is unintelligible
                print("Sorry, I did not understand that.")

            except sr.RequestError:
                # In case of a network issue or API problem
                print("Sorry, there was an error with the API request.")
                break


if __name__ == "__main__":
    live_transcribe()
