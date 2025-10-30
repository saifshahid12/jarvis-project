import speech_recognition as sr
import webbrowser
import pyttsx3
import music_liabrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
from dotenv import load_dotenv
import os
# pip istall pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = " "

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the mp3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the mp3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stop playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def aiProcess(command):
    # Configure gemini with your google api key
    genai.configure(api_key = "AIzaSyBM14vRkb86-2ZwQKEo9RfQLaGIHRpvOb8")

    # Create the model (you can use gemini-2.5-flash or gemini 2.5 pro)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # Generate the response
    response = model.generate_content([
        "You are a virtual assistant name Jarvis skilled in genetal tasks like Alixa and Google cloud.",
        command
    ])

    # Return the text result
    return response.text

def prcessCommand(c):

    if"open google" in c.lower():
        webbrowser.open("https:/google.com")
    elif"open youtube" in c.lower():
        webbrowser.open("https:/youtube.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("https:/linkedin.com")
    elif c.lower() .startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_liabrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}") # get from headlines by news api
        if r.status_code==200:
            # parse the jaison response
            data = r.json()

            # extract the article
            articles=data.get("articles",[])

            # print the headlines 
            for article in articles:
                speak(article['title'])
    
    else:
        # GenAi handle the request
        output = aiProcess(c)
        speak(output)
        



if __name__ =="__main__":
    speak("initializing jarvis...")
    while True:
        # isten for the wake word "jarvis.."
        # obtain audio from micropgone.
        r=sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            
            if(word.lower()=="jarvis"):                                          
                speak("yes")
                # listen for command 
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source,)
                    command = r.recognize_google(audio)

                    prcessCommand(command)
        except Exception as e:
            print(f"error; {0}".format(e))     # use f after change myself
      
