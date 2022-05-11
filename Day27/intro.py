from tkinter import *

#Setting up the window settings.
window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text='I am a label', font=('Arial', 24, "bold"))

#Pack our label on to the screen.
my_label.grid(column=0, row=0)
my_label.config(text='New Text')


#Button
def button_clicked():
    print('I got clicked')
    my_label.config(text=input.get())

button = Button(text='Click Me!', command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text='Lemon')
button2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)



#Keeps the window open.
window.mainloop()