from tkinter import *

window = Tk()   #open GUI Window

# Button
b1 = Button(window , text="Submit") # declared but no shown
        # b1.pack() This will involve but at its own fixed poaion

        #So best way is
b1.grid(row=0,column=0)

# Input 
e1=Entry(window)
e1.grid(row=0, column=1)

# Text Box
# t1 =Text(window,height=1,width=15) # It is same as input box
t1 =Text(window,height=5,width=15)
t1.grid(row=0,column=2)
       # Height and Width of text box is very big 
       # Have dto do it manually





window.mainloop()  # Keeping the window open
