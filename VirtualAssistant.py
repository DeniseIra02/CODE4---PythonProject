import speech_recognition as sr

__listener__ = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = __listener__.listen(source)
        command = __listener__.recognize_google(voice)
        print(command)
        
except:
    pass