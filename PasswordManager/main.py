from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_site = web_site_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        web_site: {
            "email": email,
            "password": password,
        }
    }

    if len(web_site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
    except:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    finally:
        web_site_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    web_site = web_site_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
            if web_site in data:
                email = data[web_site]["email"]
                password = data[web_site]["password"]
                messagebox.showinfo(title=web_site, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="No Data Found")
    except:
        messagebox.showinfo(title="Error", message="No Data Found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_site_label = Label(text="Website:")
web_site_label.grid(row=1, column=0)
web_site_entry = Entry(width=27)
web_site_entry.grid(row=1, column=1, columnspan=1)
search_entry = Button(text="Search", command=find_password)
search_entry.grid(row=1, column=2, columnspan=1)

email_label = Label(text="Email/UserName:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "newmri@naver.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=27)
password_entry.grid(row=3, column=1, columnspan=1)

generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
