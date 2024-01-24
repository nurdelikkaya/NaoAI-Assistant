from naoqi import ALProxy
import time
# Connect to the NAOqi API
nao_ip = "10.1.94.38"  # replace with the actual IP address of your NAO robot
port = 9559
motion_proxy = ALProxy("ALMotion", nao_ip, port)
# autonmus_live=ALProxy("ALAutonomousLife",nao_ip,port)
# autonmus_live.setState("disabled")
# Create an ALTextToSpeech proxy
try:
    # Create an ALTextToSpeech proxy
    tts = ALProxy("ALTextToSpeech", nao_ip, port)
except Exception as e:
    print("Error initializing ALTextToSpeech proxy: %s" % e)
try:
    posture_proxy=ALProxy("ALRobotPosture",nao_ip,port)
    posture_proxy.goToPosture("stand",1.0)
    # Define joint names for the right arm
    right_arm_joint_names = ["LShoulderRoll", "LShoulderPitch","LElbowRoll", "LElbowYaw", "LWristYaw"]

    # Set initial positions
    initial_positions = [1, 0.0,0.0, 0.0, 0.0]
    motion_proxy.angleInterpolationWithSpeed(right_arm_joint_names,initial_positions , 0.2)
    position2 = [1.0,-1.7 ,-1.0, 0.0, 0.0]
    motion_proxy.angleInterpolationWithSpeed(right_arm_joint_names,position2 , 0.2)
    position3 = [1.0,-1.7, -0.1, 0.0, 0.0]
    motion_proxy.angleInterpolationWithSpeed(right_arm_joint_names,position3 , 0.2)
    position4 = [1.0,-1.7, -1.0, 0.0, 0.0]
    motion_proxy.angleInterpolationWithSpeed(right_arm_joint_names,position4 , 0.2)

    # Wait for the waving movement to complete
    time.sleep(2.0)
    tts.say("hello")
    # Reset the arm to the initial position


except Exception as e:
    print("Error:", e)
