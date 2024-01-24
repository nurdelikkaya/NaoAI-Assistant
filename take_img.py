from naoqi import ALProxy
import os
import paramiko
# Replace these with your robot's IP address and port
robot_ip = "10.1.95.105"
robot_port = 9559

# Create a proxy to ALPhotoCapture
try:
    photoCaptureProxy = ALProxy("ALPhotoCapture", robot_ip, robot_port)
except Exception as e:
    print "Error when creating ALPhotoCapture proxy:"
    print str(e)
    exit(1)

# Set the camera resolution and picture format
photoCaptureProxy.setResolution(2)  # 2 corresponds to VGA resolution
photoCaptureProxy.setPictureFormat("jpg")

# Specify the folder and file name for the captured picture
folder_path = "/home/nao/recordings/cameras/"
file_name = "captured_image.jpg"

# Take a picture and save it to the specified folder
photoCaptureProxy.takePictures(1, folder_path, file_name)

print "Picture taken and saved to {}{}".format(folder_path, file_name)

def send_to_pc():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(robot_ip, username="nao", password="nao")
    sftp = ssh.open_sftp()
    remote_path=  "/home/nao/recordings/cameras/captured_image.jpg"
    #local_path = r'D:\Hossam\Pepper-master - Copy\audio.wav'
    local_path = r'./image.jpg'
    sftp.get(remote_path,local_path)
    #subprocess.Popen(["scp nao@pepper.local:/home/nao/audio.wav D:\Hossam"])
    #subprocess.Popen(["scp", "nao@pepper.local:/home/nao/audio.wav", rD:\Hossam"])
    sftp.close()
    ssh.close()
send_to_pc()