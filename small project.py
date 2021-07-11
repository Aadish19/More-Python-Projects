# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 22:52:46 2021

@author: adish
"""

def question_finder(sentence):
    params = ('why','how','what','who')
    capital=sentence.capitalize()
    
    if sentence.startswith(params):
        return '{}?'.format(capital)
    else:
        return '{}.'.format(capital)
    
data=[]
while True:
    datainput = input("Type the sentence")
    if datainput=='stop' or datainput=='Stop':
        break
    else:
        data.append(question_finder(datainput))
print(" ".join(data))
