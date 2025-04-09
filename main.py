import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pygame
import time
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def play_startup_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/startup.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, Tejaswi")
    elif 12 <= hour < 18:
        speak("Good afternoon, Tejaswi")
    else:
        speak("Good evening, Tejaswi")
    speak("JARVIS online. How can I help you?")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return ""

def ask_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are JARVIS, a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        return "Sorry, I couldn't reach ChatGPT."

def run_jarvis():
    play_startup_sound()
    greet_user()
    while True:
        query = listen_command()
        if not query:
            continue

        if "stop" in query or "exit" in query or "goodbye" in query:
            speak("Shutting down. Goodbye, Tejaswi!")
            break
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        else:
            response = ask_chatgpt(query)
            speak(response)

if __name__ == "__main__":
    run_jarvis()