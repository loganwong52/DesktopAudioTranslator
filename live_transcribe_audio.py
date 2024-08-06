import speech_recognition as sr
import threading


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


def recognize_audio(recognizer, audio, language):
    try:
        try:
            text = recognizer.recognize_google(audio, language=language)
            print(f"{text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an error with the request.")
        except sr.WaitTimeoutError:
            print("silence -> timedout")
    except KeyboardInterrupt:
        print("Stopping...")


def live_transcribe(device_index, lang):
    language = set_language(lang)
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
                        target=recognize_audio, args=(recognizer, audio, language)
                    ).start()
                except sr.WaitTimeoutError:
                    print("silence")
                    # pass  # Handle timeout errors silently

        listen_thread = threading.Thread(target=listen_and_transcribe)
        listen_thread.start()

        try:
            while True:
                pass  # Keep the main thread alive
        except KeyboardInterrupt:
            print("Stopping...")


# Run live transcription with the correct device index
live_transcribe(device_index=1, lang="e")
