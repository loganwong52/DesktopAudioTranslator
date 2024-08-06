import pyaudio
import speech_recognition as sr

# Initialize recognizer and PyAudio
recognizer = sr.Recognizer()
p = pyaudio.PyAudio()
device_index = 4

# Open the stream using the default input device (e.g., microphone)
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024,
)

print("Listening...")

try:
    while True:
        # Read data from the stream
        data = stream.read(1024, exception_on_overflow=False)

        # Convert the data to audio data
        audio_data = sr.AudioData(data, 44100, 2)

        try:
            # Recognize speech using Google Web Speech API, set language to French
            # text = recognizer.recognize_google(audio_data, language="fr-FR")
            text = recognizer.recognize_google(audio_data, language="en")
            print("Vous avez dit: " + text)
        except sr.UnknownValueError:
            print("Google Web Speech could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech; {e}")

except KeyboardInterrupt:
    print("Stopping...")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()
