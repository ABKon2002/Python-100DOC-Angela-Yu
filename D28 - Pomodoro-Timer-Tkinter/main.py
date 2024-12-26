
from tkinter import *
from math import floor

DYELLOW = "#FFB200"
ORANGE = "#EB5B00"
DPINK = "#D91656"
VIOLET = "#640D5F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0

window = Tk()
window.title("Pomodoro Timer")
window.config(pady = 50, padx = 100, bg = VIOLET)



# TODO : Timer Reset

# TODO : Timer Mechanism

# TODO : Countdown Mechanism (for testing purposes)
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count >= 0:
        # print(count)
        canva.itemconfig(timer_text, text = f"{count_min:02d}:{count_sec:02d}")
        window.after(1000, count_down, count - 1)

def update_reps():
    global reps
    if reps < 8:
        reps += 1
    elif reps == 8:
        reps = 0
    checkmark_label.config(text = CHECK_MARK * reps)

# TODO : UI setup
canva = Canvas(width = 200, height = 235, bg = VIOLET, highlightthickness = 0)   # The last parameter is to remove the border
tomato_img = PhotoImage(file = "D28 - Pomodoro-Timer-Tkinter\\tomato.png")
canva.create_image(100, 120, image = tomato_img)
timer_text = canva.create_text(115, 147, text = "00:00", fill = DYELLOW, font = (FONT_NAME, 30, "bold"))
canva.grid(row = 1, column = 1)

# Adding components:
# Timer heading
heading_label = Label(text = "Timer", fg = DPINK, bg = VIOLET, font = (FONT_NAME, 50, "bold"))
heading_label.grid(row = 0, column = 1)

# Start button
def start_timer():
    global reps
    work_sec = 10 # WORK_MIN * 60
    short_break_sec = 5 # SHORT_BREAK_MIN * 60
    long_break_sec = 15 # LONG_BREAK_MIN * 60
    # If its the 1st, 3rd, 5th, 7th rep --> Work for 25 mins
    if reps % 2 == 1:
        count_down(work_sec)
    # If its the 2nd, 4th, 6th rep --> Short break for 5 mins
    if reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
    # If its the 8th rep --> Long break for 20 mins
    if reps == 8:
        count_down(long_break_sec)
    update_reps()

start_button = Button(text = "Start", 
                      highlightthickness = 0, 
                      bg = ORANGE, 
                      fg = "black", 
                      font = (FONT_NAME, 15, "bold"),
                      command = start_timer)
start_button.grid(row = 2, column = 0)

# Pause Button
def pause_timer():
    pass
pause_button = Button(text = "Pause", 
                      highlightthickness = 0, 
                      bg = ORANGE, 
                      fg = "black", 
                      font = (FONT_NAME, 15, "bold"))
pause_button.grid(row = 2, column = 2)

# Reset Button
# reset_button = Button(text = "Reset", 
#                       highlightthickness = 0, 
#                       bg = ORANGE, 
#                       fg = "black", 
#                       font = (FONT_NAME, 15, "bold"))
# reset_button.grid(row = 2, column = 2)

# Checkmarks to denote the number of sessions completed.
checkmark_label = Label(text = CHECK_MARK, 
                        fg = "green", 
                        bg = VIOLET, 
                        font = (FONT_NAME, 15, "bold"))
checkmark_label.grid(row = 3, column = 1)

# count_down(10)

window.mainloop()