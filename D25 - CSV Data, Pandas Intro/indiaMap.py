import pandas as pd
from turtle import Turtle, Screen, shape
from scoreboard import Scoreboard
from states import States
import time

# Setting up the screen
screen = Screen()
screen.setup(width = 650, height = 800)
screen.bgcolor("black")
screen.title("India States Game")
image = "D25 - CSV Data, Pandas Intro\\Data\\IndiaMap.gif"
screen.addshape(image)
shape(image)

scoreboard = Scoreboard(map = 'IND')

state_cursor = States('D25 - CSV Data, Pandas Intro\Data\Indian_states.csv')

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
