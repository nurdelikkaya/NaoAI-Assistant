from naoqi import ALProxy
import time
import os
import paramiko

# Set the IP address and port of your NAO robot
nao_ip = "10.1.95.105"
nao_port = 9559

# Create ALAutonomousLife proxy
life_proxy = ALProxy("ALAutonomousLife", nao_ip, nao_port)

# Create ALAudioRecorder proxy
audio_recorder = ALProxy("ALAudioRecorder", nao_ip, nao_port)

# Create ALMemory proxy for speech recognition
memory_proxy = ALProxy("ALMemory", nao_ip, nao_port)

# Create an ALTextToSpeech proxy
tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)

# Set the target word to listen for
target_word = "hello"

# Set the file path and name for the recording
file_path = "/home/nao/audio.wav"

# Set the text content you want NAO to say
x = "hello, how can I help you"

# Variable to track whether recording is active
recording_active = False

# Function to start recording
def start_recording():
    global recording_active
    if not recording_active:
        time.sleep(5)
        audio_recorder.startMicrophonesRecording(file_path, "wav", 16000, [0, 0, 1, 0])
        print("Recording...")
        recording_active = True

# Function to stop recording
def stop_recording():
    global recording_active
    if recording_active:
        audio_recorder.stopMicrophonesRecording()
        print("Recording stopped.")
        send_to_pc()
        recording_active = False

# Function to send the recorded file to the PC
def send_to_pc():
    # Your existing code for SSH and file transfer
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(nao_ip, username="nao", password="nao")
    sftp = ssh.open_sftp()
    remote_path = "/home/nao/audio.wav"
    local_path = r'./audio.wav'
    sftp.get(remote_path, local_path)
    sftp.close()
    ssh.close()

# Function to handle the word recognized event
def on_word_recognized(value):
    word = value[0]
    confidence = value[1]

    # Check if the recognized word is the target word with sufficient confidence
    if word == target_word and confidence > 0.5:
        # Stop recording and send to PC when the target word is detected
        print("done")
        tts.say(x)
        time.sleep(5)
        stop_recording()

# Subscribe to the speech recognition event
memory_proxy.subscribeToEvent("WordRecognized", "SpeechRecognitionModule", "on_word_recognized")

# Enable autonomous life
life_proxy.setState("solitary")

# Main loop to keep the program running
try:
    while True:
        start_recording()
        time.sleep(1)
except KeyboardInterrupt:
    # Unsubscribe from the event and disable autonomous life on program exit
    memory_proxy.unsubscribeToEvent("WordRecognized", "SpeechRecognitionModule")
    life_proxy.setState("disabled")
