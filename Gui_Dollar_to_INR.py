from tkinter import *

window = Tk()

def conversion():
    # print(dollars.get())
    # indianrupees = (dollars.get())*75 >>>>>It will give the output 75 times bcoz its a string



        
    
    
    dollars = (float(indianrupees.get())/75)
    t1.delete("1.0",END) # It will help deleting the previous Output
    t1.insert(END,dollars) # END is used ki jab user multiple times submit karega toh usse aage aayega naaki replace karega 
    
    euros = (float(indianrupees.get())/(88.60))
    t2.delete("1.0",END)
    t2.insert(END,euros)

    canadian = (float(indianrupees.get())/(60.39))
    t3.delete("1.0",END)
    t3.insert(END,canadian)

b1 = Button(window,text="Convert", command=conversion) 
# command gives funtionality 
b1.grid(row = 0, column=0)

#Input
indianrupees = StringVar() # StringVar() = will give user input
e1 = Entry(window,textvariable = indianrupees)
e1.grid(row=1,column=1)



#TextBox
t1 = Text(window,height=1,width=12)
t1.grid(row=2,column=0)

t2 = Text(window,height=1,width=12)
t2.grid(row=2,column=1)

t3 = Text(window,height=1,width=12)
t3.grid(row=2,column=2)


window.mainloop()