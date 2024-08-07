# DesktopAudioTranslator
The main file to run is live_transcribe_audio.py

This program can access your desktop audio and transcribe it live.
It can understand English, and translate French or Japanese into English.

Sadly, it is NOT VERY GOOD at detecting audio. (Garbage in, Garbage Out)
Also, it doesn't transcribe very quickly, and may miss some words.

So less background noise is good.
Audio that is slow speech is good.

I thought this would be an ingenius way for me to understand French & Japanese movies with no English subtitles, or French Twitch streamers.
Sadly, it's quite honestly trash.
_________________
ctrl+shift+p
Then: select python interpretor
Set it to anaconda
_________________
1. Installing pyaudio SpeechRecognition:
sudo apt-get update
sudo apt-get install python3-pyaudio python3-dev build-essential
pip install pyaudio SpeechRecognition
pip install googletrans==4.0.0-rc1

2. Install VB Cable
Install VB-Audio Virtual Cable from the VB-Audio website.
Unzip and extract files to a new folder in Program Files
Right click the VBCABLE_Setup_x64.exe and select "Run as Administrator"

3. Setting up VB Cable
Set the Virtual Cable as the Default Playback Device:
Go to Sound Settings by doing
Windows + R
type in: control
In the control panel, click on Sound
Under the Recording tab, set "CABLE Output" as the default device.
Note: In the Playback tab, you'll see "CABLE Input"

_______________________
Setting up the sound correctly so this program can pick it up.
1. In VoiceMeeter, set A1 to Headphones. Set A2 to CABLE Input (VB-Audio Virtual Cable).
2. Then, Click on "Menu" in the upper right corner
3. Hover over Shortcut Hook >
4. Click on Hook Volume Keys (For Level Output A1). This lets your volume keys control the volume for your headphones again.

5. In Computer Settings>System>Sound 
set Output to Voicemeeter Input and 
set Input to Voicemeeter Out B1

6. Go to Control Panel > Sound
7. In the Playback tab, set Voicemeeter Input as Default
8. In the Recording tab, set Voicemeeter Out B1 as Default

Basically, how this works is, you have to match the Default Recording aka Input audio device
with whatever device_index you pass into live_transcribe() function in transcribe_audio.py

You can double check the device_index by running check_devices.py

9. Play your video

10. Run transcribe_audio.py by clicking the triangle

