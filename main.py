import tkinter as tk
from tkinter import PhotoImage, Entry, Label, Button, messagebox

from PIL.Image import Image, ImageTK


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if len(website_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showwarning(title="Missing Fields", message="All fields must be filled!")
        return

    is_ok = messagebox.askokcancel(title=website_text,message=f"These are the dtails entered:\n\nEmail:{email_text}\nPassword: {password_text}\n\nDo you want to save?")

    if is_ok:
        with open("details.txt", "a") as f:
            f.write(f"{website_text} | {email_text} | {password_text}\n")

        website_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = tk.Canvas(window,width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=0,columnspan=3)
#Website
website_label = Label(text="Website:")
website_label.grid(row = 1,column=0,sticky="E")
website_entry = tk.Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2,sticky="W")

#Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0,sticky="E")
email_entry = tk.Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky="W")

#Password
password_label = Label(text="Password:")
password_label.grid(row=3,column=0,sticky="E")
password_entry = tk.Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2,sticky="W")

#Buttons
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky="EW")

window.mainloop()