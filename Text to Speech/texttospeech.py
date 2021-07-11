import gtts
from gtts import gTTS
import os #This module is used to play the converted video

myText = "A paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea. Paragraphs add one idea at a time to your broader argument."

#i wanted to set language to english
language ='en'

output = gTTS(text=myText,lang=language,slow=False)

#The file is converted Now I want to save it as an mp3 file
output.save("output.mp3")

#NOw we want our lap to automatically play the audio
os.system("start output.mp3")