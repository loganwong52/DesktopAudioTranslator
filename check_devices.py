import pyaudio

# Initialize PyAudio
audio = pyaudio.PyAudio()


def list_all_available_audio_devices():
    # List all available audio devices
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']}")


# Voicemeeter Input? NO
# Voicemeeter Out A2? NO
# Voicemeeter Out A1? NO
# "CABLE Output" NO
# Voicemeeter Out A5: 4, 28, 61
# Voicemeeter Out B1: 1, 25, 64
# Headphones: 13, 37, 51,


def get_info_about_device(device_index):
    # Specify the index of the input device
    # Get the device info
    device_info = audio.get_device_info_by_index(device_index)
    print(f"Device {device_index}: {device_info['name']}")
    print(f"Max input channels: {device_info['maxInputChannels']}")


def list_some_audio_devices():
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


def display_info_given_device_index(device_index):
    print("Available audio devices:")
    for i in range(audio.get_device_count()):
        if i == device_index:
            device_info = audio.get_device_info_by_index(i)
            print(f"Device {i}: {device_info['name']}")
            print(f"    Max input channels: {device_info['maxInputChannels']}")
            print(f"    Max output channels: {device_info['maxOutputChannels']}")
            print(f"    Default sample rate: {device_info['defaultSampleRate']}")
            print(f"    Host API: {device_info['hostApi']}")
            print(f"    Sample format: {device_info.get('sampleFormat', 'Unknown')}")
            print(f"    Default sample rate: {device_info['defaultSampleRate']}\n")
            return


list_all_available_audio_devices()
# get_info_about_device(4)
# list_some_audio_devices()
# display_info_given_device_index(4)

# I was thinking, maybe I didn't need a VB-audio cable, and maybe I could just
# connect my headphones to my code, but no, it fails because it has 0 input channels.
# At least 2 input channels are needed for the code to work...
# Headphones: 13, 37, 51
# get_info_about_device(13)
# get_info_about_device(37)
# get_info_about_device(51)

# Terminate PyAudio instance
audio.terminate()
