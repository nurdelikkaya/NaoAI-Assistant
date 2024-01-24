import speech_recognition as sr
import json
def audio_to_text(audio_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_path) as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        try:
            # Listen for speech
            audio = recognizer.record(source)
            # Perform speech-to-text
            text = recognizer.recognize_google(audio)
            text= {"role": "user", "content": f'{text}'}
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

# Example usage
audio_path = r"D:/college/projects/cognitive_poject/venv/text_generator/audio.wav"

transcription = audio_to_text(audio_path)

if transcription:
    print("Transcription:")
    print(transcription)
else:
    print("Transcription failed.")
text_file_path = "D:/college/projects/cognitive_poject/venv/text_generator/textfile.txt"
with open(text_file_path, 'w', encoding='utf-8') as file:
    # Convert the dictionary to a JSON-formatted string
    transcription_str = json.dumps(transcription)
    file.write(transcription_str)

print("File written successfully.")