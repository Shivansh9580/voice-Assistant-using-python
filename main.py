# import win32com.client
#
# speaker=win32com.client.Dispatch("SAPI.SpVoice")
#
# while 1:
#     print("enter the word you want to speak it out by me:")
#     s=input()
#     speaker.speak(s)
import pyttsx3 as p
import speech_recognition as sr

r = sr.Recognizer()
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hii, How can I help you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    while 1:
        print("listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        speak(text)
     # speaker.say("Hello Shivansh. My name is Jarvis")