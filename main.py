import calendar
import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import random
import wikipedia
import webbrowser
import ctypes
import winshell

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices') #Getting details of current voice
engine.setProperty('voice', voices[0].id) #Changing index, changes voices. 0 for male
#engine.setProperty('voice', voices[1].id) #Changing index, changes voices. 1 for female

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

# def rec_audio():
#     recog = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         print("Recording...")
#         audio = recog.listen(source)
#
#     data = " "
#
#     try:
#         data = recog.recognize_whisper(audio,language="english")
#         print("You said: " + data)
#
#     except sr.UnknownValueError:
#         print("Assistant could not understand the audio")
#
#     except sr.RequestError as ex:
#         print("Request Error from Google Speech Recognition" + ex)
#
#     return data
#
# recog = sr.Recognizer() # initialise a recogniser
# def record_audio():
#     with sr.Microphone() as source: # microphone as source
#         print("ask...")
#         audio = recog.listen(source, 5, 5)  # listen for the audio via source
#         print("Done Listening")
#         voice_data = ''
#         try:
#             voice_data = recog.recognize_google(audio)  # convert audio to text
#         except sr.UnknownValueError: # error: recognizer does not understand
#             print('I did not get that')
#             talk('I did not get that')
#         except sr.RequestError:
#             print('Sorry, the service is down') # error: recognizer is not connected
#         return voice_data.lower()

def record_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data

def response(text):
    #talk(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)

def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return f'Today is {week_now}, {months[month_now -1]} the {ordinals[day_now -1]}.'

def say_hello(text):
    greet = {"hi", "hola", "hey", "greetings", "hello", "salut", "bonjour", "quoi de neuf", "halo", "hey there"}

    response = {"hi", "hola", "hey", "greetings", "hello", "salut", "bonjour", "quoi de neuf", "halo", "hey there"}

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i+1].lower() == "is":
            return list_wiki[i+2] + "" + list_wiki[i+3]





while True:
    try:
        text = record_audio()
        speak = " "

        if call(text):
            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text or "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                     meridiem = "p.m"
                     hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is" + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text or "who is" in text or "what is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            elif "who are you" in text or "define yourself" in text or "tell me more about you" in text:
                speak = speak + """Hey, I am your personal voice assistant to assist you in anything"""

            elif "your name" in text:
                speak = speak + "my name is Arise"

            elif "who am I" in text:
                speak = speak + "You are surely a human"

            elif "why do you exist" in text:
                speak = speak + "To serve you onee-chan"

            elif "fine" in text or "good" in text:
                speak = speak + "Good to know"

            elif "where do you come from" in text:
                speak = speak + "Go ask your mom"

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "opening Google Chrome"
                    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

                elif "word" in text.lower():
                    speak = speak + "opening word"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

                elif "excel" in text.lower():
                    speak = speak + "opening excel"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

                elif "powerpoint" in text.lower() or "power point" in text.lower():
                    speak = speak + "opening powerpoint"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")

                elif "vs code" in text.lower() or "visual studio" in text.lower():
                    speak = speak + "opening visual studio code"
                    os.startfile(r"C:\Users\lion\AppData\Local\Programs\Microsoft VS Code Insiders\Code - Insiders.exe")

                elif "codeblock" in text.lower() or "code block" in text.lower():
                    speak = speak + "opening codeblock"
                    os.startfile(r"C:\Program Files\CodeBlocks\codeblocks.exe")

                elif "youtube" in text.lower():
                    speak = speak + "opening Youtube"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "opening Google"
                    webbrowser.open("https://google.com/")

                elif "stackoverflow" in text.lower() or "stack overflow" in text.lower():
                    speak = speak + "opening Stackoverflow"
                    webbrowser.open("https://stackoverflow.com/")

                elif "facebook" in text.lower():
                    speak = speak + "opening Facebook"
                    webbrowser.open("https://youtube.com/")

                else:
                    speak = speak + "Application not available"

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind+1:]
                webbrowser.open("http://www.youtube.com/results?search_query="+"+".join(search))
                speak = speak + "Openining" + str(search) + " on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "change background" in text or "change wallpaper" in text:
                img = r'C:\Users\lion\Downloads\Wallpapers'
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background changed successfully"

                
                
            response(speak)

    except:
        response("I don't know that")




