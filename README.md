# Voice Recognition Using Python

This project demonstrates how to use Python's `speech_recognition` library to recognize and convert spoken words into text using the Google Web Speech API.

## Features
- Captures audio input through the microphone.
- Converts speech to text in real-time.
- Provides error handling for unrecognized audio or network issues.

## Prerequisites
Ensure you have the following installed:
- Python 3.6 or higher
- The `speech_recognition` library

To install the required library, run:
```bash
pip install SpeechRecognition
```

## How to Use
### 1.Clone this repository:
```bash
git clone https://github.com/shabeer-10/Voice_Recognition.git
cd Voice_Recognition
```

### 2.Run the script:
```bash
python voice_recognition.py
```

### 3.Speak into your microphone when prompted.

## Error Handling
-If the audio is unclear, the program will inform you: `Sorry, I could not understand the audio.`
-If there's an issue with the API or network: `Could not request results; check your network connection.`

## Notes
-Ensure your microphone is enabled and functioning.
-The Google Web Speech API requires an active internet connection.

## Contributions
Feel free to fork the repository, improve the code, and submit a pull request.

## License
This project is licensed under the MIT License.

