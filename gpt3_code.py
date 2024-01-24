# import openai
# from gtts import gTTS
# import os
# import speech_recognition as sr
# import speech_recognition_code 
# # Set up API key
# openai.api_key = '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'

# # Create a conversation list
# conversation = []

# # Start the conversational loop
# audio_path = r"D:/college/projects/cognitive_poject/venv/audio.wav"

# # while True:
# #     # Add the user's message to the conversation
# #     conversation.append({"role": "user", "content": user_input})

# # Send the conversation to the GPT model


# if __name__ == "__main__":
#     transcription = speech_recognition_code.audio_to_text(audio_path)
#     conversation.append(transcription)
#     response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=conversation
#     )
#     # Extract the model's text response
#     model_response = response['choices'][0]['message']['content']
#     print(model_response)
#     # Convert the text response to speech and play it
#     # tts = gTTS(text=model_response, lang='en')
#     # tts.save("response.mp3")

import openai
import os
import speech_recognition as sr
import speech_recognition_code

# Set up API key
openai.api_key = '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'

# Create a conversation list
conversation = []

# Start the conversational loop
file_content=''
audio_path = r"D:/college/projects/cognitive_poject/venv/text_generator/textfile.txt"
with open(audio_path, 'r') as file:
        # Read the entire content of the file as a single string
        file_content = file.read()
        print("File Content:")
        print(file_content)
conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant in college of artificial intelligence your name is nao robot and you live in the college lab provides responses within 20 words.'}   
]
if __name__ == "__main__":
    # Recognize speech from the audio file
    transcription = file_content
    conversation.append(transcription)
    
    # Send the conversation to the GPT model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    # Extract the model's text response
    model_response = response['choices'][0]['message']['content']
    
    # Print the response
    print(model_response)
    
    # Save the response to a text file
    text_file_path = "D:/college/projects/cognitive_poject/venv/text_generator/gpt_response.txt"
    with open(text_file_path, 'w', encoding='utf-8') as file:
        file.write(model_response)

