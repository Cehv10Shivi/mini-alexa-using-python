import sys # to access amy function
import pyttsx3 # for text to speach
import pywhatkit #for playing songs on youtube
import speech_recognition as sr # for speech recognition
import datetime # for date and time
import wikipedia # for searching in wikipedia
import webbrowser # for opening web browser
import os
import pyjokes  # for jokes

import flask   # my program shows error . to run  pywhatkit i use this( for creating web application)

def voice(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        voice("GOOD MORNING SHASHI KANT SIR")

    elif hour>=12 and hour<18:
        voice("good afternoon SHASHI KANT SIR")   

    else:
        voice("Good Evening SHASHI KANT SIR!")  

    voice("I AM ASSISTANT OF ABHIJEET AND SHIVANI  WHAT CAN I DO FOR U  ")       

def takeCommand():                    #take command from microphone
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said:",query)

    except Exception as e:  
            print("Say  again ...")  
            return "None"
    return query


if __name__ == "__main__":
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   #id=0 for male and id =1 for  female

    wishMe()

    while True:
        query = takeCommand().lower()
        # conditional statements for taking command
        if 'play song from youtube' in query:
            song = query.replace('play song from youtube', '')
            voice('playing ' + song) 
            pywhatkit.playonyt(song) # inbuild function for playing song from youtube

        elif 'wikipedia' in query:
            voice('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results.encode("utf-8")) #  special type of encoding
            voice("According to Wikipedia")
            voice(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")   


        elif 'play songs from device' in query:
            music_dir = 'C:\\Users\\HP\\Music\\Video Projects'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif ' time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print("current time is",time)
            voice('Current time is ' + time)


        elif 'date' in query:
            voice('sorry, I have a headache')

        elif 'are you single' in query:
            voice('I am in a relationship with alexa friend')

        elif 'how are you' in query:
            voice('i am fine')
            voice('how are you')

        elif 'I am also fine' in query:
            voice('hope you will')

        elif 'joke' in query:
            voice(pyjokes.get_joke())
            voice('ha ha ha ha ha ha')
        elif 'stop' in query:
            print("thank you")
            sys.exit()
