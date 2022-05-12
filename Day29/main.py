from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #This adds to our alpha numeric list that is our password a random selection of characters ranging from 8 to 10, symbols from 2 to 4 and 2 to 4 numbers.
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(letters) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    #Append all of our letters numbers and symbols into a single list.
    password_list = password_letters + password_symbols + password_numbers

    #shuffle around all the letters numbers and symbols.
    shuffle(password_list)

    #Join the list of letters numbers and symbols into a string.
    password = ''.join(password_list)

    #When the generate passwword button is clicked we fill the entry box with the newly conjoined string.
    password_entry.insert(0, password)

    #After generating the password, it is saved into our clipboard for pasting.
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    #Check if the website or password entries are empty.
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        #Verify whether or not what they user has entered is correct before saving via pop-up box.
        is_ok = messagebox.askokcancel(title= website_entry.get(), message=f"These are the details entered: \nEmail: {email_entry.get()}"
                                                                   f"\nPassword: {password_entry.get()} \nIs it okay to save?")
        #If they are satisfied with their entry write to a new file or create a new one containing their password. 
        if is_ok:
            with open("Day29\\SavedPasswords.txt", "a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    


# ---------------------------- UI SETUP ------------------------------- #
#Create window with padding.
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Create Canvas.
canvas = Canvas(height=200, width=200)

#Allocate logo and pull it into canvas.
logo_img = PhotoImage(file="Day29\images\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "YourEmail@Platform.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column =1)


#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



canvas.grid()
window.mainloop()