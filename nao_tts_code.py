from naoqi import ALProxy
import time

# Set the IP address and port of your NAO robot
nao_ip = "10.1.95.105"
nao_port = 9559

# Create an ALTextToSpeech proxy
try:
    # Create an ALTextToSpeech proxy
    tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
except Exception as e:
    print("Error initializing ALTextToSpeech proxy: %s" % e)
file_content=""
# Set the text content you want NAO to say
file_path="D:/college/projects/cognitive_poject/venv/text_generator/gpt_response.txt"
try:
    with open(file_path, 'r') as file:
        # Read the entire content of the file as a single string
        file_content = file.read()
        print("File Content:")
        print(file_content)
except Exception as e:
    print("Error reading file: %s" % e)
    

# file_content="bla bla "
# audio_file_path = "D:/college/projects/cognitive_poject/venv/nao_audio.wav"

# Say the text and save it to the file
tts.say(file_content)

# Wait for the speech to finish
time.sleep(5)  # Adjust the sleep duration based on the length of the speech

# Release the proxy
