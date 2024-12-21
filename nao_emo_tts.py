import os
import subprocess

# Paths for Piper and TTS files
piper_executable = "./piper"  # Path to the Piper binary
piper_model = "./tr_TR-medium.onnx"  # Path to the Turkish Piper model (.onnx file)
output_audio_path = "./nao_audio.wav"  # Output audio file path
text_file_path = "D:/college/projects/cognitive_poject/venv/text_generator/gpt_response.txt"  # Text input file

def text_to_speech_piper(text, model_path, output_path):
    """
    Convert text to speech using Piper and save it as a .wav file.
    Args:
        text (str): The text to be converted to speech.
        model_path (str): Path to the Piper model.
        output_path (str): Path to save the generated audio file.
    Returns:
        bool: True if the TTS was successful, False otherwise.
    """
    try:
        # Prepare the command for Piper
        command = [piper_executable, "--model", model_path, "--output_file", output_path]

        # Use subprocess to run Piper
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=text.encode("utf-8"))

        # Check if Piper executed successfully
        if process.returncode == 0:
            print("TTS completed successfully. Audio saved at:", output_path)
            return True
        else:
            print("Piper TTS failed. Error message:", stderr.decode("utf-8"))
            return False

    except Exception as e:
        print("Error during TTS processing:", str(e))
        return False


# Read the content of the text file
try:
    with open(text_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read().strip()
        print("Text Content:", file_content)
except Exception as e:
    print("Error reading text file:", str(e))
    file_content = ""

# Perform text-to-speech with Piper if there is content to process
if file_content:
    success = text_to_speech_piper(file_content, piper_model, output_audio_path)
    if success:
        print("The audio is ready to play!")
    else:
        print("Failed to generate audio.")
else:
    print("No text content to process.")
