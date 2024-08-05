# import pyaudio

# # Initialize PyAudio
# audio = pyaudio.PyAudio()

# # List all available audio devices
# for i in range(audio.get_device_count()):
#     info = audio.get_device_info_by_index(i)
#     print(f"Device {i}: {info['name']}")

# audio.terminate()

# Voicemeeter Input I guess is what I want?
# 13, 37, or 53
# NO!
# Voicemeeter Out A2 instead?
# 1, 25, 60
# Voicemeeter Out A1 instead?
# 10, 34, 68

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
        if maxInputChannels > 0:
            print(f"Device {i}: {device_info['name']}")
            print(f"    Max input channels: {device_info['maxInputChannels']}")

    # Terminate PyAudio instance
    audio.terminate()


list_audio_devices()
