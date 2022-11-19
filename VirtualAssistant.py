import speech_recognition as sr
import pyttsx3

__listener__ = sr.Recognizer()
__engine__ = pyttsx3.init()

__engine__.say("Hi, I am you Jazz")
__engine__.say("Tell me what will I do for you")
__engine__.runAndWait()

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