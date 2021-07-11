#!/usr/bin/env python
# coding: utf-8

# In[67]:


import random
from datetime import datetime

def get_greet(h):
    h=datetime.now().hour
    
    if h>=5 and h<12:
        return ("Good Morning")
    elif h>=12 and h<=16:
        return ("Good afternoon")
    elif h>16 and h<=24:
        return ("Goog Evening")
    elif h>24 and h<5:
        return ("Good midnight")
        
def heelohi(x):
    inputs = ["Hello","Hey","Hii","What's Up","Hola"]
    value = random.choice(inputs)
    return value

user_name = input("What's your name \n\n")
print(f"{heelohi(value)} {user_name},{get_greet(h)}")

game = input("Would yo like to play a guess game [Y/N] \n\n")
if game == 'Y' or game == 'y' or game == 'yes' or game == 'Yes':
    print("Okay Then Get Started")
    
    r = random.randint(1,11)
    print("I am thinking of a random number between 1 and 10 \n\n")
    
    random = r
    count = 0
    for i in range(10):
        user_guess = int(input("\n You guess \n"))
        if user_guess == random:
            print("Brilliant Guess")
            
            break
        elif user_guess < random:
            print("Think Higher")
            count+=1
            continue
        elif user_guess > random:
            print("Guess Smaller")
            count+=1
            continue
        else:
            print(" Type Valid Number Between 1 and 10")
    print(f"You have Guessed in {count} times")
    
    
else:
    print("Ooh, Okay")
    


# In[48]:


import random
r = random.randint(1,11)
random = r
random


# # Gives Random Strings

# In[60]:


import random
inputs = ["Hello","How Are Youhh","How's Your Health"]
value = random.choice(inputs)
print(value)


# In[ ]:




