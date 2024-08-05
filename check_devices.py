import pyaudio

# Initialize PyAudio
audio = pyaudio.PyAudio()

# List all available audio devices
for i in range(audio.get_device_count()):
    info = audio.get_device_info_by_index(i)
    print(f"Device {i}: {info['name']}")

audio.terminate()
