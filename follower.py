from naoqi import ALProxy
import time

# Connect to the robot
ip = "10.1.95.105"  # Replace with the actual IP address of your robot
port = 9559
waving_detection = ALProxy("ALWavingDetection", ip, port)
tts = ALProxy("ALTextToSpeech", ip, port)

# Subscribe to the waving event
waving_detection.subscribe("WavingDetection/Waving")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user")
    print("Stopping...")

# Unsubscribe from the waving event
# waving_detection.unsubscribe("WavingDetection/Waving")



hyft7 rshoulderoll go negative 
hyrf3 pitch shouldrr nhyt negative 
hyrf3 elbowroll nhyt 2 
make from wrisy yaw men +ve le negative 