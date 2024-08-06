import speech_recognition as sr


def set_language(lang):
    """
    Takes in an abreviated language,
    returns the language code for Google Translate
    """
    # Language codes:
    # https://www.science.co.il/language/Locale-codes.php
    language = ""
    if lang == "Fr" or lang == "fr" or lang == "f":
        language = "fr-fr"
    elif lang == "j":
        language = "ja"
    elif lang == "e":
        language = "en-us"
    else:
        print("Your entered language is unrecognized. Set to English by Default")
        language = "en-us"
    return language


def live_transcribe(device_index, lang):
    """
    Listens to a given audio device for a given language.
    Live transcribes any speech that is heard in the terminal.

    device_index: int that is the index of the audio device to listen to
    lang: string abreviation, either e, f, or j
    """
    language = set_language(lang)

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Set up the microphone or virtual audio device
    with sr.Microphone(
        device_index=device_index, sample_rate=44100, chunk_size=2048
    ) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            while True:
                try:
                    audio = recognizer.listen(source)
                    # Recognize speech using Google Web Speech API
                    text = recognizer.recognize_google(audio, language=language)

                    print(f"Transcription: {text}")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand the audio.")
                except sr.RequestError:
                    print("Sorry, there was an error with the request.")

        except KeyboardInterrupt:
            print("Stopping...")


# Run live transcription with the correct device index
# 1, 25, 64 = Voicemeeter Out B1 (VB-Audio Vo)
live_transcribe(device_index=1, lang="e")

"""
The device_index must match the default Recording in Control Panel > Sound
"""
