from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
generate_password_button = Button(text='Generate Password')
generate_password_button.grid(column=2, row=3)

#Create the Add button
add_button = Button(text='Add', width= 44)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()