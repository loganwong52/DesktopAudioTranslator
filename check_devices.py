# import pyaudio

# # Initialize PyAudio
# audio = pyaudio.PyAudio()

# # List all available audio devices
# for i in range(audio.get_device_count()):
#     info = audio.get_device_info_by_index(i)
#     print(f"Device {i}: {info['name']}")

# audio.terminate()

# Voicemeeter Input? NO
# Voicemeeter Out A2? NO
# Voicemeeter Out A1? NO
# "CABLE Output" instead does work...
# 4, 28, 62, 105

########################################################
# import pyaudio

# # Initialize PyAudio
# audio = pyaudio.PyAudio()

# # Specify the index of the input device
# device_index = 68  # Replace with the correct index

# # Get the device info
# device_info = audio.get_device_info_by_index(device_index)
# print(f"Device {device_index}: {device_info['name']}")
# print(f"Max input channels: {device_info['maxInputChannels']}")

# # Terminate PyAudio instance
# audio.terminate()

import pyaudio


def list_audio_devices():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    print("Available audio devices:")
    for i in range(audio.get_device_count()):
        device_info = audio.get_device_info_by_index(i)
        maxInputChannels = device_info["maxInputChannels"]
        name = device_info["name"]
        if (
            "Voicemeeter Input" not in name
            and "A2" not in name
            and "A1" not in name
            and "CABLE Output" not in name
            and maxInputChannels > 0
        ):
            print(f"Device {i}: {device_info['name']}")
            print(f"    Max input channels: {device_info['maxInputChannels']}")
            print(f"    Max output channels: {device_info['maxOutputChannels']}")
            print(f"    Default sample rate: {device_info['defaultSampleRate']}")
            print(f"    Host API: {device_info['hostApi']}")
            print(f"    Sample format: {device_info.get('sampleFormat', 'Unknown')}")
            print(f"    Default sample rate: {device_info['defaultSampleRate']}\n")

    # Terminate PyAudio instance
    audio.terminate()


list_audio_devices()


# 62 seems to work. "CABLE Output"
# 4, 28, 62, 105

# Initialize PyAudio
# audio = pyaudio.PyAudio()

# # Print information for the device
# device_index = 62  # Replace with your device index
# device_info = audio.get_device_info_by_index(device_index)
# print(device_info)

# audio.terminate()
