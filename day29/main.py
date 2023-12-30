import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip
import json

BACK_DROP = "#d3d3de"
TEXT_TUP = ("Agency FB", 12, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():

    chars = string.ascii_letters
    nums = "0123456789"
    special = "!@\"'/\\#$%^&*()+="

    random_pass = random.choices(chars, k=8) + random.choices(nums, k=4) + random.choices(special, k=4)
    random.shuffle(random_pass)
    random_pass = "".join(random_pass)

    passwd_box.delete(0, tk.END)
    passwd_box.insert(0, random_pass)
    pyperclip.copy(random_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():

    website = site_box.get()
    email = uname_box.get()
    password = passwd_box.get()
    json_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    if password == "":
        messagebox.showwarning(title="Empty Field", message="Password field left blank")
    elif email == "":
        messagebox.showwarning(title="Empty Field", message="Email/Username field left blank")
    elif website == "":
        messagebox.showwarning(title="Empty Field", message="Website field left blank")
    else:

        msg = f"Website: {website}\nEmail/Username: {email}\nPassword: {password}\n" \
              f"Are you sure you want to save this password?"

        response = messagebox.askquestion("Confirmation", msg)

        if response == "yes":

            try:
                passwd_file = open("./password.json", mode="r")
            except FileNotFoundError:
                with open("./password.json", mode="w") as passwd_file:
                    json.dump(json_entry, passwd_file, indent=3)
            else:
                json_data = json.load(passwd_file)
                json_data.update(json_entry)
                passwd_file.close()
                passwd_file = open("./password.json", mode="w")
                json.dump(json_data, passwd_file, indent=3)
                passwd_file.close()

            messagebox.showinfo("", "Password saved successfully")

# ---------------------------- SEARCH FUNCTION ------------------------------- #

def search():

    try:
        passwd_file = open("./password.json", mode="r")
    except FileNotFoundError:
        messagebox.showinfo("", f"Password file not found")
    else:
        passwords = json.load(passwd_file)
        for search_site in passwords:
            website = site_box.get()
            if search_site == website:
                messagebox.showinfo("", f"Website: {website}\n"
                                        f"Email: {passwords[search_site]['email']}\n"
                                        f"Password: {passwords[search_site]['password']}")
                return 0

        messagebox.showinfo("", f"No password found for website: {site_box.get()}")

# ---------------------------- UI SETUP ------------------------------- #


# Instantiate a window, set title and padding
window = tk.Tk()
window.title("MyPass")
window.config(pady=20, padx=20, bg=BACK_DROP)

# Create the lock PhotoImage, then put it into the canvas
lock = tk.PhotoImage(file="./logo.png")
lock_canvas = tk.Canvas(window, width=200, height=200, bg=BACK_DROP, highlightthickness=0)
lock_canvas.create_image(100, 100, image=lock)


# Create the labels for input information
site = tk.Label(text="Website:", width=10, bg=BACK_DROP, font=TEXT_TUP)
uname = tk.Label(text="Email/Username:", bg=BACK_DROP, font=TEXT_TUP)
passwd = tk.Label(text="Password:", bg=BACK_DROP, font=TEXT_TUP)

# Create text boxes
site_box = tk.Entry(width=29, font=TEXT_TUP)
uname_box = tk.Entry(width=51, font=TEXT_TUP)
passwd_box = tk.Entry(width=29, font=TEXT_TUP)

# Create buttons
gen = tk.Button(text="Generate Password", width=20, command=gen_pass, font=TEXT_TUP)
add = tk.Button(text="Add", width=60, command=add_pass, font=TEXT_TUP)
search = tk.Button(text="Search", width=20, command=search, font=TEXT_TUP)

# Packing of logo
lock_canvas.grid(column=1, row=0)

# Packing of the labels (LHS)
site.grid(column=0, row=1, padx=5)
uname.grid(column=0, row=2, padx=5)
passwd.grid(column=0, row=3, padx=5)

# Packing of text entries (MIDDLE)
site_box.grid(column=1, row=1, columnspan=1, pady=5)
uname_box.grid(column=1, row=2, columnspan=2, pady=2)
passwd_box.grid(column=1, row=3, pady=5)

# Packing of buttons (As necessary)
gen.grid(column=2, row=3, pady=5, padx=10)
add.grid(column=1, row=4, columnspan=2)
search.grid(column=2, row=1, pady=5, padx=10)


window.mainloop()
