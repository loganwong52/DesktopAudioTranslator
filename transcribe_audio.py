import speech_recognition as sr


def live_transcribe(device_index):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Set up the microphone or virtual audio device
    with sr.Microphone(
        device_index=device_index, sample_rate=44100, chunk_size=2048
    ) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        while True:
            try:
                audio = recognizer.listen(source)
                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio)
                print(f"Transcription: {text}")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Sorry, there was an error with the request.")


# Run live transcription with the correct device index (replace 62 with your device index)
live_transcribe(device_index=62)
