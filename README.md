# DesktopAudioTranslator
1. Installing pyaudio SpeechRecognition:
sudo apt-get update
sudo apt-get install python3-pyaudio python3-dev build-essential
sudo pip install pyaudio SpeechRecognition

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

____________________
ctrl+shift+p
Then: select python interpretor
Set it to anaconda

_______________________
Setting up the sound correctly so this program can pick it up.
1. In VoiceMeeter, set A1 to headphones

2. In Computer Settings>System>Sound set Output to 
Voicemeeter Input and set Input to 

3. Go to Control Panel > Sound

4. In the Playback tab, set Voicemeeter Input as Default

5. In the Recording tab, set Voicemeeter Out B1 as Default

6. Play your video

7. Run Transcribe_audio.py

