from email import message
from urllib import response
from dotenv import load_dotenv
import requests, pyttsx3, time, speech_recognition as sr, openai, os
load_dotenv()

openai.api_key = os.getenv("OPENAI")
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

r, mic = sr.Recognizer(), sr.Microphone()

def callback(recognizer, audio, text=""):
    try: text = recognizer.recognize_google(audio, language="en-IN")
    except: pass;
    if(not text): return;
    print("You said:", text)
    message = text
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print("Sambit Said:", reply)
    pyttsx3.speak(reply)

with mic as source:
    start_msg = "Sambit is as your service!"
    print(start_msg)
    pyttsx3.speak(start_msg)
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 0.5

r.listen_in_background(mic, callback, phrase_time_limit=3)

while True: time.sleep(5)