"""
Author: Logan Wong
8/5/2024
"""

import speech_recognition as sr


def transcribe_audio_file(file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(file_path) as source:
        # Adjust for ambient noise (optional, usually used for live audio)
        recognizer.adjust_for_ambient_noise(source)

        # Extract audio data from the file
        audio_data = recognizer.record(source)

        # Recognize speech using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"Transcription: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an error with the request.")


# Path to your WAV file
file_path = "output.wav"

# Run transcription on the specified audio file
transcribe_audio_file(file_path)
