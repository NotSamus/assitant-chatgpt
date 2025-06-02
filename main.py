# Code designed and implemented by Jesus R. Lopez
import os
from openai import OpenAI
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np

load_dotenv()
model = 'gpt-3.5-turbo' 

r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
greetings = ["Hey kids", "yeah?"]
client = OpenAI(api_key=os.getenv('KEY'))

def listen_for_wake_word(source):
    print("Listening for 'Hey Pete'...")
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "hey pete" in text.lower():
                print("Wake word detected.")
                engine.say(np.random.choice(greetings))
                engine.runAndWait()
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass


def listen_and_respond(source):
    print("Listening...")
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if not text:
                continue
            response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": f"{text}"}]) 
            response_text = response.choices[0].message.content
            print(f"OpenAI response: {response_text}")
            engine.say(response_text)
            engine.runAndWait()

            if not audio:
                listen_for_wake_word(source)
        except sr.UnknownValueError:
            time.sleep(2)
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()
            listen_for_wake_word(source)
            break
with sr.Microphone() as source:
    listen_for_wake_word(source)
