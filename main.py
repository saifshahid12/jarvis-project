import speech_recognition as sr
import webbrowser
import pyttsx3
import music_liabrary
import requests
# pip istall pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="ef500f2f2db04d67bd67e38216163489"     # api get from web (news api)

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
      
