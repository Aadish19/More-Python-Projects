import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

#2nd Step - Adding Backend
answers=["America","India","Asia"]

questions=[]

for i in answers:
    words = list(i)
    shuffle(words) # Shuffling the list
    questions.append(words)

num = random.randint(0,len(questions)-1)

def initial():
    global questions , num
    lb1.configure(text=questions[num])

#3rd Step -Giving Functinality to Buttons
# Check Button
def answercheck():
    global answers,questions,num,words
    userinput = e1.get()
    if userinput == answers[num]:
        messagebox.showinfo("Success","Winner !!")
    else:
        messagebox.showinfo("Error","Oops!!,Try again")
        e1.delete(0,END) #After checking once the input box will become empty

# Reset Button
def resetswitch():
    global questions,words,answers
    num = random.randint(0,len(questions)-1)
    lb1.configure(text=questions[num])
    
    e1.delete(0,END)
# answercheck()

# 1st Step - Making window
window = Tk()
window.geometry("400x400")
window.configure(background="#46B2E0")
window.title("JumbleBot")
window.iconbitmap(r"icon.ico")

lb1 = Label(window, font="times 20",bg="#F4BE2C",fg="#FF6666")
lb1.pack(pady=30,ipady=10,ipadx=10)

answer = StringVar()
e1=Entry(window,textvariable = answer)
e1.pack(ipady=5,ipadx=5)

button1 = Button(window, text="check",bg="#758283",width=20,command=answercheck)
button1.pack(pady=40)

button2 = Button(window, text="Reset",bg="#CAD5E2",width=20,command=resetswitch)
button2.pack()

# just calling the funcion
initial()

# 4th Step
# Color Schemes
# Google: www.uicolorpicker.com
# fg bg background added





window.mainloop() 