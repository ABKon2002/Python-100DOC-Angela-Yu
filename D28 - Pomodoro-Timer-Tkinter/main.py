from tkinter import *
from math import floor
from data import motivational_quotes, user_guide_sentences
import random

# Constants
DYELLOW = "#FFB200"
ORANGE = "#EB5B00"
DPINK = "#D91656"
VIOLET = "#640D5F"
FONT_NAME = "Courier"
COUNT = 0
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
NOT_CHECK_MARK = "✘"
BULLS_EYE = "🎯"
STATUS_STRING = []
TIMER = None
SESSIONS_LIST = ["Lets Start working!", "Slow down :)⌛", "Get Ready!💪", 
                 "Work🛠️", "Short Break🧘", "Long Break⏸️", "Another Session?⚡"]
REPS = 1

# Functions needed:

def start_timer():
    generate_a_thought()
    # Making the start button turn into a reset button, when start is clicked.
    start_button.config(text = "Reset",
                        command = timer_reset)
    global REPS
    global STATUS_STRING
    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # Long Break session
    if REPS % 8 == 0:
        REPS = 1
        STATUS_STRING.pop()
        STATUS_STRING.append(CHECK_MARK)
        checkmark_label.config(text = ''.join(STATUS_STRING), fg = "green")
        session_label.config(text = SESSIONS_LIST[5], font = (FONT_NAME, 30, "normal"))
        count_down(long_break_sec)
        ask_for_another_session()
    # Short Break session
    elif REPS % 2 == 0:
        REPS += 1
        STATUS_STRING.pop()
        STATUS_STRING.append(CHECK_MARK)
        checkmark_label.config(text = ''.join(STATUS_STRING), fg = "green")
        session_label.config(text = SESSIONS_LIST[4], font = (FONT_NAME, 30, "normal"))
        count_down(short_break_sec)
    # Work session 
    else:
        REPS += 1
        STATUS_STRING.append(NOT_CHECK_MARK)
        checkmark_label.config(text = ''.join(STATUS_STRING), fg = "green")
        session_label.config(text = SESSIONS_LIST[3], font = (FONT_NAME, 30, "bold"))
        count_down(work_sec)

def count_down(count):
    global COUNT
    COUNT = count
    count_min = floor(count / 60)
    count_sec = count % 60
    if count >= 0:
        global TIMER
        canva.itemconfig(timer_text, text = f"{count_min:02d}:{count_sec:02d}")
        TIMER = window.after(1000, count_down, count - 1)
        if count == 5:
            # Bring the window to the front
            window.deiconify()
            window.lift()
            window.attributes('-topmost', True)  # Keep window on top
            window.attributes('-topmost', False)
            if REPS % 2 == 0:
                session_label.config(text = SESSIONS_LIST[1], font = (FONT_NAME, 30, "normal"))
            else:
                session_label.config(text = SESSIONS_LIST[2], font = (FONT_NAME, 30, "normal"))
    if count == 0:
        start_timer()

def timer_reset():
    # Making the reset button turn into a start button, when reset is clicked.
    start_button.config(text = "Start", command = start_timer)
    window.after_cancel(TIMER)
    canva.itemconfig(timer_text, text = "00:00")
    quote_label.config(text = "Let's start working! :)")
    checkmark_label.config(text = NOT_CHECK_MARK, fg = "black")
    global STATUS_STRING
    STATUS_STRING = []
    global REPS
    REPS = 1

def generate_a_thought():
    thoughts = motivational_quotes + (user_guide_sentences * 3)   # Making the guides 3 times more likely...
    current_thought = random.choice(thoughts)
    quote_label.config(text = current_thought)
    window.after(90000, generate_a_thought)     # Generating a random thought every 30 seconds...

def pause_timer():
    # Turn the pause button to the resume button, when pause is clicked,
    pause_button.config(text = "Resume", command = resume_timer)
    window.after_cancel(TIMER)

def resume_timer():
    # turn the resume button into the pause button, when resume is clicked, 
    pause_button.config(text = "Pause", command = pause_timer)
    window.after(1000, count_down, COUNT)

def ask_for_another_session():
    window.after_cancel(TIMER)
    start_button.config(text = "Start", command = start_timer)
    global REPS
    REPS = 1
    session_label.config(text = SESSIONS_LIST[6], font = (FONT_NAME, 30, "bold"))
    for _ in range(4):      # Replacing 4 check marks with a bulls-eye emoji
        STATUS_STRING.remove(CHECK_MARK)
    STATUS_STRING.remove("\t")
    STATUS_STRING.append(BULLS_EYE)
    STATUS_STRING.append("\t")
    checkmark_label.config(text = ''.join(STATUS_STRING), fg = "green")


# GUI window setup
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width = 620, height = 550)
window.config(pady = 50, padx = 50, bg = VIOLET)


# Window Components:

# Timer heading (and sessions)
session_label = Label(text = "POMO Timer", fg = DPINK, bg = VIOLET, font = (FONT_NAME, 50, "bold"))
session_label.grid(row = 0, column = 1)

# Quotes label
quote_label = Label(text = "Let's start working! :)", fg = "black", bg = VIOLET, font = (FONT_NAME, 15, "normal"),
                      wraplength = 400)
quote_label.grid(row = 1, column = 1)

# The Tomato canva with the timer text
canva = Canvas(width = 200, height = 235, bg = VIOLET, highlightthickness = 0)   # The last parameter is to remove the border
tomato_img = PhotoImage(file = "D28 - Pomodoro-Timer-Tkinter\\tomato.png")
canva.create_image(100, 120, image = tomato_img)
timer_text = canva.create_text(115, 147, text = "00:00", fill = DYELLOW, font = (FONT_NAME, 30, "bold"))
canva.grid(row = 2, column = 1)

# Start button (& Reset button, they toggle between each other)
start_button = Button(text = "Start", 
                      highlightthickness = 0, 
                      bg = ORANGE, 
                      fg = "black", 
                      font = (FONT_NAME, 15, "bold"),
                      command = start_timer)
start_button.grid(row = 3, column = 0)

# Pause Button (& Resume button, they toggle between each other)
pause_button = Button(text = "Pause", 
                      highlightthickness = 0, 
                      bg = ORANGE, 
                      fg = "black", 
                      font = (FONT_NAME, 15, "bold"),
                      command = pause_timer)
pause_button.grid(row = 3, column = 2)

# Checkmarks to denote the number of sessions completed.
checkmark_label = Label(text = NOT_CHECK_MARK, 
                        fg = "black", 
                        bg = VIOLET, 
                        font = (FONT_NAME, 15, "bold"))
checkmark_label.grid(row = 4, column = 1)

# To denote what the checkmarks mean,
checkmark_meaning = Label(text = "Completed Sessions", 
                          fg = "black",
                          bg = VIOLET, 
                          font = (FONT_NAME, 15, "normal"))
checkmark_meaning.grid(row = 5, column = 1)


window.mainloop()
