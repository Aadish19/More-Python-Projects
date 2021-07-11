# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:40:17 2021

@author: adish
"""
# import sys
# sys.builtin_module_names

import time
import os
import pyttsx3

while True:
    
    if os.path.exists("contents.txt"):
        with open("contents.txt") as contents:
            file = contents.read()
            print(file)
    else:
        os.system("start Notepad")
        pyttsx3.speak("Bhakk Bhadwe")
    time.sleep(3)
    
