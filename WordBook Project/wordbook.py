# Given Is JSON File 
#Here The user will enter a word 
#We will process the key in json file 
#If its directly found then give the Value
#If not then It will check for key which has same spelling as key in JSON file

#When no key then Error == User Friendly Message

# IMPORTANT THING --===== When we have to compare words either nearer to correct word or incorrect word
    #1.>>> from difflib import SequenceMatcher
     #2 >>> SequenceMatcher(None , "treee","tree")
   # <difflib.SequenceMatcher object at 0x00000265B50F6E50>
    #3 >>> SequenceMatcher(None , "treee","tree").ratio()
      # 0.8888888888888888  <<_------Giving probability of match

      #Method       =     get_close_matches
     # 1111111111111111)))))) from difflib import get_close_matches
     # help(get_close_matches)
     # >>> get_close_matches(word ,possibilities,n=3,cutoff = 0.6)

# get_close_matches
# >>> from difflib import get_close_matches
# >>> get_close_matches("treee",["tree","dog","cat"])
# ['tree']  ==<< closest match


#                       First Work Is to convert JSON file to PYTHON Readable Format
#Process ==

# 1. import json
# 2. elements = json.load(open("wordbook.json"))
  
#   To Check 
# 1.  type(elements)
# 2. print(elements)
# ---------------------
# Now can find the key and its value by

# 3. elements["tree"]


# Basic Code
# import json
# elements = json.load(open("wordbook.json"))

# def findmeaning(word):
#     return elements[word]

# word = "tree"

# print(findmeaning(word))

                                                        # Using get_close_match
# import json
#import difflib
# from difflib import get_close_matches
# elements = json.load(open("wordbook.json"))
# a=elements.keys()
# get_close_matches("treee",a)
# ['tree', 'three', 'tree ear']  =>> Closest match first
# get_close_matches("treee",a,n=1)
# ['tree']
# get_close_matches("treee",a)[0]
# 'tree'

                                    # n only gives the 3 nearer word but cutoff also checks the best closer word

# get_close_matches("goddd",a,cutoff=0.5)
# ['odd', 'god', 'good']
# get_close_matches("goddd",a,cutoff=0.9)
# [] ==>> Coz no word which is very close to 'goddd'

#User friendly Program
import json
from difflib import get_close_matches

elements = json.load(open("wordbook.json"))

def findmeaning(word):
    
    if word.lower() in elements:
        return elements[word.lower()]
# Only Lower is not applicable for 'USA' , 'Paris'
    elif word.upper() in elements:
            return elements[word.upper()]
    elif word.title() in elements:
            return elements[word.title()]

    elif len(get_close_matches(word,elements.keys()))>0:
        closestmatch = get_close_matches(word,elements.keys())[0]
        # user_decision = input(f"Are yot looking for {closestmatch} instead [Y/N]") OR
        user_decision = input("Are yot looking for %s instead [Y/N] ?  " % closestmatch)

        if user_decision == "Y":
            return elements[get_close_matches(word,elements.keys())[0]]
        
        elif user_decision == "N":
            return "I cant find your word"
        else:
             return "Unable to conclude at proper output,Somry"
            
    else:
        return "I can't find this word. Please look for spelling mistakes"

word = input("Type any word to get its meaning: ")


# print(findmeaning(word)) =>It is giving output as a List 

output = findmeaning(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)












