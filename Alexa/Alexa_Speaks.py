# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:31:35 2021

@author: adish
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.say()
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening------")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
           

    except:
        pass

    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        sing = command.replace('play','')
        talk('playing',+sing)
        pywhatkit.playonyt(sing)
    elif 'time' in command:
        time = datetime.dataetime.now().strftime('%I:%M %p')
        print(time) 
        talk('Current time is' + time)
    
    elif 'wikipedia' in command:
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
     elif 'jokes' in command:
         joke = pyjokes.get_joke()
         print(joke)
         talk(joke)
    else:
        talk('Please say command again')

while True:
    run_alexa()