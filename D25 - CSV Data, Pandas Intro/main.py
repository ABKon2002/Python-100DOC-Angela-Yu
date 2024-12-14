import pandas as pd
from turtle import Turtle, Screen, shape
from scoreboard import Scoreboard
from states import States
import time

# Setting up the screen
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("US States Game")
image = "D25 - CSV Data, Pandas Intro\\Data\\blank_states_img.gif"
screen.addshape(image)
shape(image)

# def get_mouse_click_coor(x, y):
#     X.append(x)
#     Y.append(y)
#     print(x, y)

scoreboard = Scoreboard()

state_cursor = States()

score = 0
strikes = 0
while score < 50 and strikes < 3:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        exit()
    if state_cursor.reveal_state(answer_state):
        scoreboard.ding_ding()
        score += 1
    else:
        scoreboard.striked()
        strikes += 1

scoreboard.game_over()
time.sleep(3)
exit()

screen.mainloop()
