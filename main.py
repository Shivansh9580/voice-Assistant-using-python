
import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *

r = sr.Recognizer()
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello, how are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    print("listening...")
    r.adjust_for_ambient_noise(source, 1.2)
    try:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
        text = ""

if "what" and "about" and "you" in text:
    speak("I am also fine")

speak("How can I help you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    print("listening...")
    r.adjust_for_ambient_noise(source, 1.2)

    try:
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
        text2 = ""

if "information" in text2:
    speak("About which topic do you need information")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        print("listening...")
        r.adjust_for_ambient_noise(source, 1.2)

        try:
            audio = r.listen(source)
            infor = r.recognize_google(audio)
            print(infor)
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            info = ""


    if infor:
        get_info(infor)

elif "play" or "Video" in text2:
    speak("which video you want to play")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        print("listening...")
        r.adjust_for_ambient_noise(source, 1.2)

        try:
            audio = r.listen(source)
            vid = r.recognize_google(audio)
            print(vid)
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            vid = ""

    if vid:
        play(vid)

