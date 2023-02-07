#!/usr/bin/env python3

import datetime
import getpass
import os
import smtplib
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import p as gpt
import gui
from g import search_video
import pg as run
print("Initializing Jarvis....")
master ="Prabhas"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
}
search_engines = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "bing": "https://www.bing.com",
    "spotify" :"https://open.spotify.com"
}


def open_url(url):
    webbrowser.open(url)
    chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
    webbrowser.get(chrome_path).open(url)


def search(search_query, search_engine):
    if search_engine=="https://www.youtube.com":
        open_url(search_video(search_query))
    elif search_engine=="https://open.spotify.com":
        open_url(f"https://open.spotify.com/{search_query}")
    else:
        open_url(f"https://www.google.com/search?q={search_query}")

def speak(text):
    gui.speak(text)
    engine.say(text)
    engine.runAndWait()


def print_and_speak(text):
    print(text)
    speak(text)


def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning " + master)
    elif hour < 18:
        speak("Good Afternoon " + master)
    else:
        speak("Good Evening " + master)

    # speak("Hey I am Jarvis. How may I help you")


# This is where our programme begins....


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        """The default value as per speech_recognition documentation.
        Increase if application stops responding. and decrease if
        assistant doesn't execute any command and just says next
        command sir."""

        audio = r.listen(source,5,3)

    print("Recognizing....")
    query = ""
    try:
        query = str(r.recognize_google(audio, language="en-in"))
        print("User said: "+ query) 
    except sr.UnknownValueError:
        print("Sorry could you please try again?")

    except Exception as e:
        print(e)
        print("Say that again, please?")

    return query


speak("Initializing Jarvis....")
wish_me()


def execute_the_command_said_by_user():
    query = take_command().lower()
    # logic for executing basic tasks
    if "date" in query:
        print_and_speak(f"{datetime.datetime.now():%A, %B %d, %Y}")
    elif "time" in query:
        print_and_speak(f"{datetime.datetime.now():%I %M %p}")
    elif "open" in query.lower():
        speak("Is it an app or website")
        text = take_command().lower()
        if 'app' in text:
            run.func(query.split()[-1])
        else:
            try:
                open_url(popular_websites[query.split()[-1]])
            except:  # If the website is unknown
                search(query.split("open")[-1] ,search_engines["google"])
    elif "play" in query.lower():
        text = gpt.play(query)
        search_query = text.split(":")[0]
        if 'no' not in text.split(":")[1]:
            try:
                print(text)
                search_engine = search_engines[text.lower().split(":")[-1]]
                search(search_query, search_engine)
            except:
                search(query.split(":")[-1],search_engines["youtube"])
        else:
            speak("didnt tell correct platform try again")
    elif "email" in query:
        speak("Who is the recipient? ")
        recipient = take_command()

        if "me" in recipient:
            try:
                speak("What should I say? ")
                content = take_command()

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("Your_Username", "Your_Password")
                server.sendmail("Your_Username", "Recipient_Username", content)
                server.close()
                speak("Email sent!")
            except Exception:
                speak("Sorry Sir! I am unable to send your message at this moment!")

    elif "nothing" in query or "abort" in query or "stop" in query:
        speak("okay")
        speak("Bye Sir, have a good day.")
        sys.exit()
    elif "bye" in query:
        speak("Bye Sir, have a good day.")
        sys.exit()

    elif "create" in query:
        speak("Is it File or Folder")
        speak("Playing your request")
    else:
        speak(gpt.open(query))
def exe():
    query = gui.store_value()
    # logic for executing basic tasks
    if "date" in query:
        print_and_speak(f"{datetime.datetime.now():%A, %B %d, %Y}")
    elif "time" in query:
        print_and_speak(f"{datetime.datetime.now():%I %M %p}")
    elif "open" in query.lower():
        speak("Is it an app or website")    
        text = take_command().lower()
        if 'app' in text:
            run.func(query.split()[-1])
        else:
            try:
                open_url(popular_websites[query.split()[-1]])
            except:  # If the website is unknown
                search(query.split("open")[-1] ,search_engines["google"])
    elif "play" in query.lower():
        text = gpt.play(query)
        search_query = text.split(":")[0]
        if 'no' not in text.split(":")[1]:
            try:
                print(text)
                search_engine = search_engines[text.lower().split(":")[-1]]
                search(search_query, search_engine)
            except:
                search(query.split(":")[-1],search_engines["youtube"])
        else:
            speak("didnt tell correct platform try again")
    elif "email" in query:
        speak("Who is the recipient? ")
        recipient =  gui.store_value()

        if "me" in recipient:
            try:
                speak("What should I say? ")
                content =  gui.store_value()

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("Your_Username", "Your_Password")
                server.sendmail("Your_Username", "Recipient_Username", content)
                server.close()
                speak("Email sent!")
            except Exception:
                speak("Sorry Sir! I am unable to send your message at this moment!")

    elif "nothing" in query or "abort" in query or "stop" in query:
        speak("okay")
        speak("Bye Sir, have a good day.")
        sys.exit()
    elif "bye" in query:
        speak("Bye Sir, have a good day.")
        sys.exit()
    else:
        speak(gpt.open(query))
gui.set_speak_command(execute_the_command_said_by_user)
gui.set_btn(exe)
gui.mainloop()
