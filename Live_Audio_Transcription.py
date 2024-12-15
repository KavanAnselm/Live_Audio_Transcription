import speech_recognition as sr

def callback(recognizer, audio):
    try:
        # Initializing Speech Recognition
        text = recognizer.recognize_google(audio)
        print(f"User : {text}")
    except sr.UnknownValueError:
        print("Unable to recongnize")
    except sr.RequestError as e:
        print(f"Request error for speech service; {e}")

def live_speech_to_text():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Adjust for Noise
    with microphone as source:
        print("Initializing... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
    print("Listening...")

    # Start listening & processing
    stop_listening = recognizer.listen_in_background(microphone, callback)

    # Keep executing until Ctrl+C is clicked
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Terminating when prompted
        print("\nProgram Terminated, Exiting...")
        stop_listening()

if __name__ == "__main__":
    live_speech_to_text()
