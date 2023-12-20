import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def make_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    new_password = []

    hm_letters = random.randint(8, 10)
    hm_symbols = random.randint(2, 4)
    hm_numbers = random.randint(2, 4)

    for i in range(hm_letters):
        new_password.append(letters[random.randrange(0, len(letters))])

    for j in range(hm_symbols):
        new_password.append(symbols[random.randrange(0, len(symbols))])

    for m in range(hm_numbers):
        new_password.append(numbers[random.randrange(0, len(numbers))])

    random.shuffle(new_password)

    pyperclip.copy("".join(new_password))

    if len(password_input.get()) > 0:
        password_input.delete(0, "end")
    password_input.insert(0, "".join(new_password))

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_text = website_input.get().capitalize()
    login_text = login_input.get()
    password_text = password_input.get()

    data_voc = {
        website_text: {
            "login": login_text,
            "password": password_text
        }
    }

    if login_text == '' or password_text == '' or website_text == '':
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"There are the details entered:"
                                                                   f"\nEmail: {login_text}"
                                                                   f"\nPassword: {password_text}")

        if is_ok:
            try:
                with open("data.json", "r") as data:
                    data_dict = json.load(data)
                    data_dict.update(data_voc)

            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(data_voc, data, indent=4)

            else:
                with open("data.json", "w") as data:
                    json.dump(data_dict, data, indent=4)

            website_input.delete(0, "end")
            password_input.delete(0, "end")


def search():

    new_search = website_input.get().capitalize()

    try:
        with open("data.json", "r") as data:
            data_dict = json.load(data)
            find_login = data_dict[new_search]["login"]
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for {new_search} exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        find_password = data_dict[new_search]["password"]
        messagebox.showinfo(title=new_search, message=f"Login: {find_login}\n"
                                                      f"Password: {find_password}")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")

canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=0, row=0, columnspan=3)

website = tkinter.Label(text="Website:")
website.grid(column=0, row=1, sticky="w", pady=5)

website_input = tkinter.Entry()
website_input.config(width=33)
website_input.focus()
website_input.grid(column=1, row=1, sticky="w", pady=5)

search_button = tkinter.Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1, sticky="w", pady=5, padx=5)

login = tkinter.Label(text="Login:")
login.grid(column=0, row=2, sticky="w", pady=5)

login_input = tkinter.Entry()
login_input.config(width=52)
login_input.insert(0, "khomich1022@gmail.com")
login_input.grid(column=1, row=2, columnspan=2, sticky="w", pady=5)

password = tkinter.Label(text="Password:")
password.grid(column=0, row=3, sticky="w", pady=5)

password_input = tkinter.Entry()
password_input.config(width=33)
password_input.grid(column=1, row=3, sticky="w", pady=5)

password_button = tkinter.Button(text="Generate Password", command=make_password)
password_button.grid(column=2, row=3, sticky="w", pady=5, padx=5)

add_button = tkinter.Button(text="Add", command=save)
add_button.config(width=44)
add_button.grid(column=1, row=4, columnspan=2, sticky="w", pady=5)

window.mainloop()
