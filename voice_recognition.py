import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio input
def recognize_speech_from_mic():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        # Listen for the first phrase and extract it into audio data
        audio_data = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")

# Run the voice recognition function
if __name__ == "__main__":
    recognize_speech_from_mic()
