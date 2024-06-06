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

from selenium_web import info

r = sr.Recognizer()
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello shivansh, how are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if"what"and"about"and"you"in text:
    speak("I am good")

speak("can i help you with any information?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("About which topic you need information?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    Assist = info()
    Assist.get_info("infor")