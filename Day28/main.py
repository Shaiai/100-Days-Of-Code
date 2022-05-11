from ctypes.wintypes import SHORT
from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text='Timer')
    check_marks.config(text=" ")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text ="Break", fg = RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text ="Break", fg = PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text ="Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        #Every second the function will do something.
      global timer 
      timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(floor(reps /2)):
            marks +="✔"
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
title_label.grid(column=1, row=0)

#Create a canvas to match our image size.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#Store the filepath/image into a variable using PhotoImage class.
tomato_img = PhotoImage(file="Day28\\Images\\tomato.png")

#This will pull our PhotoImage and place it on the canvas using an x and y coordinate.
canvas.create_image(100, 112, image=tomato_img)

#Creates our timer text and sets the fill and font details.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))

#This will pack all our elements into the canvas and display it to us.
canvas.grid(column=1, row=1)


#Create the start button and place it on the bottom left of the tomato.
start_button = Button(text="Start", highlightthickness=0, command = start_timer)
start_button.grid(column=0, row=2)

#Create the reset button and place it on the bottom right of the tomato.
reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer)
reset_button.grid(column=2, row=2)

#Create the checkmark and place it centered under the tomato.
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)




window.mainloop()