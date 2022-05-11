from cgitb import text
from tkinter import *

#Create our window.
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=150, height=100)
window.config(padx=10, pady=10)


#Create our inputs.
input = Entry(width=15)
input.grid(column=1,row=0)


#Create our text inputs
num_label = Label(text='Miles', font= ('Arial', 13, 'bold'))
num_label.grid(column=2, row=0)

conv_label = Label(text=f'is equal to 0 kilometers')
conv_label.grid(column=1, row=1)

#functions
def calculate():
    conv_label.config(text=f'is equal to {int(input.get()) *1.609} kilometers')

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()


