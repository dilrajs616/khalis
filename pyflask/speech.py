import speech_recognition as sr

def stt():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Convert audio to text in Punjabi (Gurmukhi script)
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="pa-IN")
        print("Transcript in Punjabi: " + text)

        # Save the transcript to a file
        with open("punjabi_transcript.txt", "w", encoding="utf-8") as file:
            file.write(text)
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    stt()
