NaoAI-Assistant
Welcome to the NaoAI-Assistant repository! This project leverages the Nao robot, utilizing its SDK and artificial intelligence capabilities to create a personalized assistant. The robot can engage in interactive conversations, recognize speech, answer questions using GPT-3.5 API, generate text-to-speech responses, and even detect facial emotions.

Table of Contents
Project Overview
Installation
Usage
File Descriptions
Contributing
License
Project Overview
nao_script.py
The nao_script.py file enables the Nao robot to initiate a conversation by asking if you have any questions. It records your answer for further processing.

speech_recognition_code.py
The speech_recognition_code.py file utilizes the SpeechRecognition library to extract text from an audio file. This is a crucial step in understanding the user's input.

gpt3_code.py
The gpt3_code.py file interacts with the GPT-3.5 API to generate intelligent responses based on the user's input. It plays a key role in providing informative and contextually relevant answers.

nao_tts_code.py
The nao_tts_code.py file uses a text-to-speech (TTS) library to convert the generated text responses into audio. This enables the Nao robot to articulate its answers in a human-like manner.

emo_detection.py
The emo_detection.py file receives an image from the Nao robot and utilizes a facial emotion detection model. This model, trained using OpenCV CascadeClassifier and TensorFlow, allows the robot to be aware of the user's facial expressions.

my_wave.py
The my_wave.py file adds a friendly touch to the interaction. When the user says "hi" to the Nao robot, it responds by saying hello while waving.

Installation
To get started, follow these steps:

Install the required dependencies.
Download the Nao SDK and set up the robot's connection.
Obtain access to the GPT-3.5 API by OpenAI.
Install the necessary Python libraries.
Usage
Run nao_script.py to initiate the conversation with Nao.
Respond to Nao's prompt, and the conversation will be recorded.
Use speech_recognition_code.py to extract text from audio files.
Utilize gpt3_code.py for intelligent responses based on the input.
Convert text to speech using nao_tts_code.py for a natural interaction.
Enable facial emotion awareness with emo_detection.py.
Enjoy a friendly interaction with Nao using my_wave.py.
File Descriptions
nao_script.py: Initiates conversation with the Nao robot.
speech_recognition_code.py: Extracts text from audio files using SpeechRecognition.
gpt3_code.py: Interacts with the GPT-3.5 API for intelligent responses.
nao_tts_code.py: Converts text to speech for the Nao robot.
emo_detection.py: Detects facial emotions using a trained model.
my_wave.py: Nao robot's friendly wave response to the user.
