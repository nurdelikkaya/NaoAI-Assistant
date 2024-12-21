import requests
import json

# Hugging Face API URL and Authorization Token
API_URL = "https://api-inference.huggingface.co/models/mpoyraz/wav2vec2-xls-r-300m-cv7-turkish"
HEADERS = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}  # Replace with your actual token

def audio_to_text(audio_path):
    """
    Transcribes an audio file to text using the Hugging Face `wav2vec2-xls-r-300m-cv7-turkish` model.
    Args:
        audio_path (str): Path to the audio file.
    Returns:
        dict or None: Transcription in JSON format or None if an error occurred.
    """
    try:
        # Read audio file
        with open(audio_path, "rb") as audio_file:
            audio_data = audio_file.read()
        
        # Send POST request to Hugging Face API
        response = requests.post(API_URL, headers=HEADERS, data=audio_data)

        # Check if the request was successful
        if response.status_code == 200:
            text = response.json()  # Extract the JSON response
            if isinstance(text, list) and len(text) > 0:  # Handle typical Hugging Face ASR response
                transcription = text[0].get("text", "")
                return {"role": "user", "content": transcription}
            else:
                print("Unexpected response format:", text)
                return None
        else:
            print(f"API request failed with status code {response.status_code}: {response.text}")
            return None

    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


# Example usage
audio_path = r"write down the audio file"  # Ensure the file is in `.flac` format

transcription = audio_to_text(audio_path)

if transcription:
    print("Transcription:")
    print(transcription)
    # Save transcription to a JSON file
    text_file_path = "D:/college/projects/cognitive_poject/venv/text_generator/textfile.txt"
    with open(text_file_path, 'w', encoding='utf-8') as file:
        transcription_str = json.dumps(transcription, ensure_ascii=False)
        file.write(transcription_str)
    print("File written successfully.")
else:
    print("Transcription failed.")
