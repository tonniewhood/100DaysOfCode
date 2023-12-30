# Imported Modules
import tkinter as tk
import pandas
import random


def yeet(garbage):
    print("yeet")


# ===== Flip the card on a space-bar press ==== #
def flip_card(junk=None):

    current_lang = card_space.itemcget(lang_label, "text")

    if current_lang == "Russian":
        card_space.itemconfig(lang_label, text="English")
        card_space.itemconfig(word_label, text=current_card["English"])
        card_space.itemconfig(card_bg, image=en_card)
    else:
        card_space.itemconfig(lang_label, text="Russian")
        card_space.itemconfig(word_label, text=current_card["Russian"])
        card_space.itemconfig(card_bg, image=ru_card)


# Get the next card
def next_card(junk):
    global current_card

    current_card = new_card(0)
    card_space.itemconfig(lang_label, text="Russian")
    card_space.itemconfig(word_label, text=current_card["Russian"])
    card_space.itemconfig(card_bg, image=ru_card)


# ========= Remove card from word-list ========= #
def remove_card(junk):
    global current_card

    row = translations[translations.Russian == current_card["Russian"]]
    idx = valid_ids.index(row.index[0])
    valid_ids.pop(idx)
    next_card(None)

    try:
        with open("./data/to_study.csv", mode="a") as study_file:
            study_file.write(str(row.index[0]) + ',' + translations.at[row.index[0], "English"] + '\n')
    except FileNotFoundError:
        with open("./data/to_study.csv", mode="w") as study_file:
            study_file.write(str(row.index[0]) +  ',' + translations.at[row.index[0], "English"] + '\n')

# ====== Generate the new card function ===== #
def new_card(junk):
    global valid_ids
    global window

    try:
        word_id = random.choice(valid_ids)
        card = {
            "English": translations["English"][word_id],
            "Russian": translations["Russian"][word_id],
        }
    except IndexError:
        card = {
            "English": "No words remaining",
            "Russian": "No words remaining",
        }

    window.after(3000, flip_card)

    return card


# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Helvetica", 40, "italic")
WORD_FONT = ("Helvetica", 60, "bold")


# Creation of the Window
window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# ====== Load CSV data on start up ======= #
try:
    translations = pandas.read_csv("./data/translation.csv")
    valid_ids = list(range(0, len(translations)))
    print(valid_ids)
except FileNotFoundError:
    current_card = {
                    "Russian": "Err",
                    "English": "Err"
    }
else:
    current_card = new_card(5)

# Creation of the Canvases
card_space = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cross_space = tk.Canvas(width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
right_space = tk.Canvas(width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)


# Creating the Photo Images
ru_card = tk.PhotoImage(file="./images/card_back.png")
en_card = tk.PhotoImage(file="./images/card_front.png")
check = tk.PhotoImage(file="./images/right.png")
cross = tk.PhotoImage(file="./images/wrong.png")


# Putting images into the canvases
card_bg = card_space.create_image(400, 263, image=ru_card)
cross_space.create_image(50, 50, image=cross)
right_space.create_image(50, 50, image=check)


# Pack the elements into the grid
card_space.grid(column=0, row=0, columnspan=2)
cross_space.grid(column=0, row=1)
right_space.grid(column=1, row=1)

# ====
lang_label = card_space.create_text(400, 163, text="Russian", font=LANG_FONT)
word_label = card_space.create_text(400, 300, text=current_card["Russian"], font=WORD_FONT)


# Monitor the "Buttons" to see if they've been pressed
cross_space.bind("<Button 1>", next_card)
right_space.bind("<Button 1>", remove_card)

window.bind("<space>", flip_card)
window.bind("<Right>", next_card)

window.mainloop()
