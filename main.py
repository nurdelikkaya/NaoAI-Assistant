import subprocess

def run_nao_code():
    subprocess.run(['python2', 'nao_script.py'])

def run_speech_recognition_code():
    subprocess.run(['python8', 'speech_recognition_code.py'])

def run_gpt3_code():
    subprocess.run(['python8', 'gpt3_code.py'])

def nao_tts_code():
    subprocess.run(['python2', 'nao_tts_code.py'])
def take_img():
    subprocess.run(['python2', 'take_img.py'])

def emo_detection():
    subprocess.run(['python8', 'emo_detection.py'])

def nao_emo_tts():
    subprocess.run(['python2', 'nao_emo_tts.py'])
def my_wave():
    subprocess.run(['python2', 'my_wave.py'])
file_content=''
audio_path = r"D:/college/projects/cognitive_poject/venv/text_generator/textfile.txt"
with open(audio_path, 'r') as file:
        # Read the entire content of the file as a single string
        file_content = file.read()
        print("File Content:")
        print(file_content)
word_list=["hello","hi"]
found_words = [word for word in word_list if word in file_content]
wordemo=["emotion","feeling","feel"]
foundemo = [word for word in word_list if word in file_content]
def main():
    run_nao_code()
    run_speech_recognition_code()
    if found_words:
        my_wave()
        run_gpt3_code()
        nao_tts_code()
    elif foundemo: 
        take_img()
        emo_detection()
        nao_emo_tts()
    else:    
        run_gpt3_code()
        nao_tts_code()
    
    

if __name__ == "__main__":
    main()
