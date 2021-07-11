import sys
from tkinter import *

def TimeTable():
    print("\n")
    for x in range(1,13):
        m = int(EnterTable.get())
        print('\t\t', 'x',(x),'=',(x*m,))

Multiply = Tk()
Multiply.geometry('250x250+700+200')
Multiply.title('Multiplication Table')

EnterTable = StringVar()

label1 = Label(Multiply,text='Multiplication Timetable', font=30 ,fg='Black').grid(row=1,column=4)
label1=Label(Multiply,text='              ').grid(row=2,column=6)
entry5 = Entry(Multiply,textvariable=EnterTable,justify='center').grid(row=3,column=4)
label1=Label(Multiply,text='              ').grid(row=2,column=6)

button1=Button(Multiply,text='Time Table',command=TimeTable).grid(row=5,column=6)
label1=Label(Multiply,text='              ').grid(row=6,column=6)
Quit = Button(Multiply,text='Quit',fg='Red',command=Multiply.destroy).grid(row=7,column=6)

Multiply.mainloop()
