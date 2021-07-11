# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:06:51 2021

@author: adish
"""

import pyttsx3
import os

engine=pyttsx3.init()
pyttsx3.speak("Enter Number To Open Application")

while True:
    print("enter Number To open Application\n")
    
    p=input()
    p=p.upper()
    print(p)
    
    if ("No" in p) or ("Not" in p) or ("DONT't" in p):
        pyttsx3.speak("Try Again and a enter a valid integer")
        
    elif('4' in p):
        os.system('start notepad')
        break
    elif ('0' in p):
        pyttsx3.speak("Exiting")
    else:
        pyttsx3.speak(p)
        print("Is Invalid ,try again")
        pyttsx3.speak("Is Invalid ,try again")
        