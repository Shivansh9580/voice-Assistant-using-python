import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
import openai

# Initialize OpenAI API
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

# Initialize text-to-speech engine
r = sr.Recognizer()
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to generate GPT-based responses
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use GPT-4 or GPT-3.5
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Sorry, I am unable to generate a response right now."


# Main assistant functionality
def voice_assistant():
    speak("Hello, how are you?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            text = ""

    if "how are you" in text.lower():
        speak("I am also fine. How can I help you today?")

    while True:
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening for your next command...")
            try:
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print(f"You said: {command}")
            except sr.UnknownValueError:
                speak("Sorry, I did not catch that.")
                command = ""

        if "exit" in command.lower():
            speak("Goodbye! Have a great day.")
            break

        elif "information" in command.lower():
            speak("About which topic do you need information?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listening for the topic...")
                try:
                    audio = r.listen(source)
                    topic = r.recognize_google(audio)
                    print(f"Topic: {topic}")
                except sr.UnknownValueError:
                    speak("Sorry, I did not catch that.")
                    topic = ""

            if topic:
                # Existing Wikipedia information retrieval
                get_info(topic)

        elif "play" in command.lower() or "video" in command.lower():
            speak("Which video would you like to play?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listening for the video...")
                try:
                    audio = r.listen(source)
                    video_query = r.recognize_google(audio)
                    print(f"Video query: {video_query}")
                except sr.UnknownValueError:
                    speak("Sorry, I did not catch that.")
                    video_query = ""

            if video_query:
                # Existing YouTube playback functionality
                play(video_query)

        else:
            # Use Generative AI for dynamic responses
            gpt_response = generate_response(command)
            print(f"GPT: {gpt_response}")
            speak(gpt_response)


# Run the voice assistant
voice_assistant()
