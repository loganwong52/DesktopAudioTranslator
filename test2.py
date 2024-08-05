import pyaudio
import speech_recognition as sr

# Initialize PyAudio
audio = pyaudio.PyAudio()


# List available audio devices
def list_devices():
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']}")


list_devices()

# Define audio stream parameters
input_device_index = 0  # Replace with the correct index for your virtual audio device
sample_rate = 44100
chunk = 1024
format = pyaudio.paInt16

# Initialize Speech Recognition
recognizer = sr.Recognizer()


def audio_callback(in_data, frame_count, time_info, status):
    audio_data = sr.AudioData(in_data, sample_rate, 2)
    try:
        text = recognizer.recognize_google(audio_data, language="en")
        print("Transcription:", text)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    return (in_data, pyaudio.paContinue)


# Open audio stream
stream = audio.open(
    format=format,
    channels=1,
    rate=sample_rate,
    input=True,
    frames_per_buffer=chunk,
    input_device_index=input_device_index,
    stream_callback=audio_callback,
)

# Start stream
stream.start_stream()

print("Listening for audio... Press Ctrl+C to stop")

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Stopping...")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
