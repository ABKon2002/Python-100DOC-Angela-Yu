
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

first_label = Label(text="I am a label", font=("Arial", 24, "bold"))
first_label.grid(row = 1, column = 0)

def name_submit():
    # print("I got clicked")
    first_label.config(text = f"Hello {entry.get()}")   # Coz it was **kwargs, we can change properties as if it is a dictionary.


entry_label = Label(text="Enter your name: ")
entry_label.grid(row = 4, column = 0)

entry = Entry(width=25)
entry.grid(row = 5, column = 0)

my_button = Button(text="Enter", command=name_submit)
my_button.grid(row = 6, column = 0)

window.mainloop()