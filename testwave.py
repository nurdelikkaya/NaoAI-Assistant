from naoqi import ALProxy
import time

# Replace with the actual IP address and port of your robot
nao_ip = "10.1.95.105"  # replace with the actual IP address of your NAO robot
port = 9559



# Resume the ASR engine
speech_recognition_proxy.pause(False)

# Subscribe to the WordRecognized event
event_name = "WordRecognized"
speech_recognition_proxy.subscribe(event_name)

try:
    print("Word spotting enabled. Say 'hi' to the robot!")

    while True:
        # Wait for the WordRecognized event
        word_event = speech_recognition_proxy.wait(event_name, 500)  # Adjust timeout as needed

        if word_event:
            # Extract information from the event
            word_detected = word_event[0]
            confidence = word_event[1]

            # Check if the detected word is "hi" with sufficient confidence
            if word_detected == "hi" and confidence > 0.5:  # Adjust confidence threshold as needed
                # Add your code to make the robot say "hi"
                print("Hi detected with confidence:", confidence)
                # Replace the print statement with code to make the robot say "hi"
                # For example, using ALTextToSpeech:
                text_to_speech = ALProxy("ALTextToSpeech", nao_ip, port)
                text_to_speech.say("Hi there!")

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Unsubscribe from the WordRecognized event
    speech_recognition_proxy.unsubscribe(event_name)
