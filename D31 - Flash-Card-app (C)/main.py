BACKGROUND_COLOR = "#B1DDC6"
CARD_TOP_FONT = ("Arial", 40, "italic")
CARD_BOTTOM_FONT = ("Arial", 60, "bold")

from tkinter import Tk, Canvas, Button, PhotoImage
from random import choice

current_card = {}

# ----------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    flash_canvas.itemconfig(card_img, image=flash_card_front_img)
    flash_canvas.itemconfig(title_text, text = "French", fill = "black")
    flash_canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    window.after(3000, flip_card)

def next_card_right():
    to_learn.remove(current_card)
    next_card()

def flip_card():
    flash_canvas.itemconfig(title_text, text = "English", fill = "white")
    flash_canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    flash_canvas.itemconfig(card_img, image=flash_card_back_img)

# ----------------------------- WINDOW SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=800, height=600)

flip_timer = window.after(3000, flip_card)

# ----------------------------- DATA ------------------------------- #
# Setting up flashcard images
flash_card_front_img = PhotoImage(file="D31 - Flash-Card-app (C)/images/card_front.png")
flash_card_back_img = PhotoImage(file="D31 - Flash-Card-app (C)/images/card_back.png")
# Setting up button images
right_img = PhotoImage(file="D31 - Flash-Card-app (C)/images/right.png")
wrong_img = PhotoImage(file="D31 - Flash-Card-app (C)/images/wrong.png")
# Setting up data (french)
from pandas import read_csv
try:
    to_learn = read_csv("D31 - Flash-Card-app (C)/data/words_to_learn.csv")
except FileNotFoundError:
    to_learn = read_csv("D31 - Flash-Card-app (C)/data/french_words.csv")
to_learn = to_learn.to_dict(orient="records")

# ----------------------------- UI SETUP ------------------------------- #
# Flash Card
flash_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = flash_canvas.create_image(400, 263, image=flash_card_front_img)
title_text = flash_canvas.create_text(400, 150, text = "Dummy", font = CARD_TOP_FONT)
word_text = flash_canvas.create_text(400, 263, text = "word", font = CARD_BOTTOM_FONT)
flash_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image = wrong_img, highlightthickness = 0, bg = BACKGROUND_COLOR, command = next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image = right_img, highlightthickness = 0, bg = BACKGROUND_COLOR, command = next_card_right)
right_button.grid(row=1, column=1)

next_card()     # Setting up the first card


window.mainloop()

from pandas import DataFrame
DataFrame(to_learn).to_csv("D31 - Flash-Card-app (C)/data/words_to_learn.csv", index=False)
