import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import spotipy
import randfacts
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from email.message import EmailMessage
from translate import Translator

#setting our engine to pyttsx3
#for text to sppech conversion
#sapi5 is the engine on microsoft

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#function to speak the text

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to wish acc to time

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 0:
        speak("happy morning")
        print("happy morning")

    elif hour >= 12 and hour < 18:
        speak("happy noon")
        print("happy noon")

    else :
        speak("happy evening")
        print("happy evening")

    assname = ("RAY")
    print("I am your assistant here")
    print(assname)
    speak("I am your assistant here")
    speak(assname)

#function to take query or the command from the user

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing.......")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said : {query}")
    except Exception as e:
        print(e)
        print("unable to recognize you")
        return "None"

    return query

#taking user name

def username():
    speak("what should I call you")
    uname = takeCommand()
    speak("welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################################")
    print(f"welcome {uname}")
    print("#####################################")

    speak("how can I help you")

def wiki(query):
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('srivarshan535@gmail.com', 'varshan@007')
    server.sendmail("srivarshan535@gmail.com", to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    #wishMe()
    #username()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            wiki(query)

        elif 'open youtube' in query:
            speak("here you go to youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("here you go to google\n")
            webbrowser.open("google.com")
             

        elif 'music' in query or "song" in query :
           clientID = "dfcae22f89a8418a82e7e9a5d42341ba"
           clientSecret = "cf33d116dc104889909281efe0d3d3f1"
           redirecturi = "http://google.com/callback/"
           oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirecturi)
           token_dict = oauth_object.get_access_token()
           token = token_dict['access_token']
           spotifyObject = spotipy.Spotify(auth=token)
           print("tell the song name")
           speak("tell the song name")
           search_song = takeCommand()
           results = spotifyObject.search(search_song, 1, 0, "track")
           songs_dict = results['tracks']
           song_items = songs_dict['items']
           song = song_items[0]['external_urls']['spotify']
           webbrowser.open(song)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'how are you' in query:
            speak("i am doing great,thank you")
            speak("how about you?")

        elif ' fine' in query or 'good' in query or 'great' in query:
            speak("its good to know that you are doing good")

        elif "what's your name" in query:
            speak("everyone calls me ")
            speak("ray")
            print("everyone calls me, ray")

        elif "exit" in query:
            speak("thanks for giving me your time")
            speak("have a great day")
            exit()

        elif 'who made you' in query or "who created you" in query:
            speak("i have been created by mr.srivarshan and bala sir")

        elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'calculate' in query:
            app_id = "E6G7H8-Y8WJX3K4L7"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("the answer is " + answer)
            speak("the answer is " + answer)

        elif 'search' in query:
            query = query.replace("search", " ")
            webbrowser.open(query)

        elif 'who I am' in query or 'who am I' in query:
            speak("if you speak you are definitely a human")
            print("if you speak you are definitely a human")

        elif 'why you came to the world' in query:
            speak('thanks to sri, further its a secret')
            print("thanks to sri, further its a secret")

        elif 'what is love' in query:
            speak('it is an emotion')
            print("it is an emotion")

        elif 'reason for you' in query:
            speak("i was created to automate the human tasks")
            print("i was created to automate the human tasks")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("hold on a sec! your system is on its way to shutdown")
            subprocess.call('shutdown / p /f')

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want sri to stop listening")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'where is' in query:
            query = query.replace("where is ", "")
            location = query
            speak("user asked to locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")

        elif 'restart' in query:
             speak("your system is on its way to restart")
             subprocess.call("shutdown / r")

        elif 'hibernate' in query or 'sleep' in query:
            speak("hibernating")
            subprocess.call("shutdown / h")

        elif 'write a note' in query or "take a note" in query:
            speak("what should i write")
            note = takeCommand()
            file = open('sri.txt', 'w')
            file.write(note)

        elif 'show note' in query or "show me the note" in query:
            speak("showing notes")
            file = open('sri.txt', 'r')
            data = file.read()
            print(data)
            speak(data)

        elif 'ray' in query:
            wishMe()
            speak("how may I help you")

        elif 'good morning' in query:
            speak("a warm" + query)

        elif 'will you marry me' in query or 'will you be my bf' in query:
            speak("sorry")
            speak(" i will not ")
            speak("you better marry a human rather than a machine")

        elif 'I love you' in query:
            speak("I love you too but as friend")

        elif 'what is' in query or 'who is' in query or "define" in query:
            client = wolframalpha.Client("E6G7H8-Y8WJX3K4L7")
            res = client.query(query)
            try:
                result = next(res.results).text
                print(result)
                speak(result)
            except:
                wiki(query)

        elif 'send a message' in query:
            speak("tell me the reciever number")
            reciever = takeCommand()
            reciever = "+91"+ reciever
            reciever = reciever.replace(" ", "")
            account_sid = "ACb44eb61c8d95096aee6a291dcb231041"
            auth_token = "4c1b3f688391c34a037ade14906de29d"
            client = Client(account_sid, auth_token)
            speak("tell the message to be sent")
            message = client.messages.create(body= "from RAY  "+takeCommand(), from_='+12542685914', to=reciever)
            print(message.sid)

        elif 'translate' in query:
            query = query.replace("translate", "")
            if 'in kannada' in query:
               query = query.replace("in kannada", "")
               translator=Translator(to_lang="kannada")
               res=translator.translate(query)
               speak(f'translating {query} in kannada')
               print(res)
               speak(res)
            elif 'in tamil' in query:
                query = query.replace("in tamil", "")
                translator = Translator(to_lang="tamil")
                res = translator.translate(query)
                speak(f'translating {query} in tamil')
                print(res)
                speak(res)
            elif 'in telugu' in query:
                query = query.replace("in telugu", "")
                translator = Translator(to_lang="telugu")
                res = translator.translate(query)
                speak(f'translating {query} in telugu')
                print(res)
                speak(res)
            elif 'in hindi' in query:
                query = query.replace("in hindi", "")
                translator = Translator(to_lang="hindi")
                res = translator.translate(query)
                speak(f'translating {query} in hindi')
                print(res)
                speak(res)
            elif 'in malayalam' in query:
                query = query.replace("in malayalam", "")
                translator = Translator(to_lang="malayalam")
                res = translator.translate(query)
                speak(f'translating {query} in malayalam')
                print(res)
                speak(res)
            elif 'in french' in query:
                query = query.replace("in french", "")
                translator = Translator(to_lang="french")
                res = translator.translate(query)
                speak(f'translating {query} in french')
                print(res)
                speak(res)


        elif 'send a mail' in query:
           try:
               speak("what should I say")
               content = takeCommand()
               speak("whom should I send")
               to = input("whom should I send")
               sendMail(to, content)
               speak("email has been sent")
           except Exception as e:
               print(e)
               print("unable to send")


        elif 'date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("The current date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'weather' in query:
            api_key = "953dcd396c15662df68383abc9ea0bf0"  
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Tell me the city")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                r = ("in " + city_name + " Temperature is " +
                     str(int(current_temperature - 273.15)) + " degree celsius " +
                     ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
                     ", humidity is " + str(current_humidiy) + " percent"
                                                               " and " + str(weather_description))
                print(r)
                speak(r)
            else:
                speak(" City Not Found ")

        elif "news" in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=f2cd4515cd334bc2b8cb10d5bc286120''')
                data = json.load(jsonObj)
                i = 1
                speak("here are some top news from times of india")
                print("====================times of India================="+'\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif "facts" in query or "fact" in query:
            x=randfacts.get_fact()
            print("did you know that,"+x)
            speak("did you know that,"+x)