"""
Author: Logan Wong
8/6/2024
"""

import speech_recognition as sr
import threading
from googletrans import Translator


def set_language(lang):
    """
    Takes in an abbreviated language,
    returns the language code for Google Translate
    """
    # Language codes:
    # https://www.science.co.il/language/Locale-codes.php
    language = ""
    if lang in ["Fr", "fr", "f"]:
        language = "fr-fr"
    elif lang == "j":
        language = "ja"
    elif lang == "e":
        language = "en-us"
    else:
        print("Your entered language is unrecognized. Set to English by default.")
        language = "en-us"
    return language


def translate_text(language, text, translator):
    """
    Takes in french or japanese text and translates it into English
    """
    # print(f"Original: {text}")
    src = ""
    if language.lower().startswith("f"):
        src = "fr"
    elif language.lower().startswith("j"):
        src = "ja"
    translation = translator.translate(text, src=src, dest="en")
    return translation.text


def recognize_audio(recognizer, audio, language, translator):
    """
    Listens to audio and transcribes it.

    If audio is too garbled/hard to understand, pass.
    If there was an error w/ request, print msg.
    If silent, pass.
    """
    try:
        try:
            text = recognizer.recognize_google(audio, language=language)

            # Translate if the language is NOT English
            if language != "en-us":
                text = translate_text(language, text, translator)

            print(f"{text}")
        except sr.UnknownValueError:
            # print("Sorry, I could not understand the audio.")
            pass
        except sr.RequestError:
            print("Sorry, there was an error with the request.")
        except sr.WaitTimeoutError:
            print("silence -> timedout")
    except KeyboardInterrupt:
        print("Stopping...")


def live_transcribe(device_index, lang):
    """
    Listens to a given audio device for a given language.
    Live transcribes any speech that is heard in the terminal.

    device_index: int that is the index of the audio device to listen to
    lang: string abreviation, either e, f, or j
    """
    # Determine the language to listen for
    language = set_language(lang)

    # Create a translator
    translator = Translator()

    # Initialize recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone(
        device_index=device_index, sample_rate=44100, chunk_size=2048
    ) as source:
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = True
        print("Listening...")

        def listen_and_transcribe():
            while True:
                try:
                    audio = recognizer.listen(source, timeout=0.5, phrase_time_limit=2)
                    threading.Thread(
                        target=recognize_audio,
                        args=(recognizer, audio, language, translator),
                    ).start()
                except sr.WaitTimeoutError:
                    # print("silence")
                    pass  # Handle timeout errors silently

        listen_thread = threading.Thread(target=listen_and_transcribe)
        listen_thread.start()

        try:
            while True:
                pass  # Keep the main thread alive
        except KeyboardInterrupt:
            print("Stopping...")


def ask_user_for_lang():
    lang = input(
        "What language will your audio be in?\nEnglish = e\nFrench = f\nJapanse = j\n"
    )
    if lang not in ["e", "f", "j"]:
        lang = "e"
    # print(lang)
    return lang


if __name__ == "__main__":
    # Prompt user to enter e, j, or f
    lang = ask_user_for_lang()

    # Run live transcription with the correct device index
    live_transcribe(device_index=1, lang=lang)
