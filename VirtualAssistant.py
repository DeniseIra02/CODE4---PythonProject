import speech_recognition as sr
import pyttsx3

__listener__ = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = __listener__.listen(source)
        command = __listener__.recognize_google(voice)
        command = command.lower()
        if 'jazz' in command:
            print(command)       
except:
    pass