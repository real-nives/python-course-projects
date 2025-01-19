from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Generates a random password with letters, symbols, and numbers.
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password_entry.delete(0, END)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

#Saves the website, email, and password to a .txt file.
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == '' or email == '' or password == '':
        messagebox.showerror(title="Shit!", message="Don't leave a field empty!")
    else:
        is_ok = messagebox.askokcancel(title="Confirm Entry", message=f"These are the details you have entered: \n\nEmail: {email}\n"
                                                      f"Password: {password}\n\nWould you like to save?")
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#Create window.
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

#Create canvas and add logo.
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(130, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website label and entry.
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

#Email label and entry.
email_label = Label(text='Email:')
email_label.grid(column=0, row=2)
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)

#Password label and entry.
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

#Create the Generate Password button.
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)

#Create the Add button
add_button = Button(text='Add', width= 44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()