import pyaudio
import wave

# Parameters
FORMAT = pyaudio.paInt16  # Format of audio
RATE = 44100  # Sampling rate (44.1kHz)
CHUNK = 1024  # Size of each audio chunk
RECORD_SECONDS = 10  # Duration to record
WAVE_OUTPUT_FILENAME = "output.wav"  # Output file name

# Initialize PyAudio
audio = pyaudio.PyAudio()

DEVICE_INDEX = 62
# Device 62: CABLE Output (VB-Audio Virtual Cable)
# Max input channels: 2

# Get Channels
device_info = audio.get_device_info_by_index(DEVICE_INDEX)
CHANNELS = device_info["maxInputChannels"]  # Number of audio channels (stereo)


# Open stream with the virtual audio device
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    input_device_index=DEVICE_INDEX,
)

print("Recording...")

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the audio data as a WAV file
with wave.open(WAVE_OUTPUT_FILENAME, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))

print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
