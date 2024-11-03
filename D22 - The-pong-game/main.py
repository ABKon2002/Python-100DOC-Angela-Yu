from turtle import Turtle, Screen
from setup import setup_screen, setup_midline
from paddle import Paddle

screen = setup_screen()
midline = setup_midline(screen)

Rpaddle = Paddle(screen, 'right')    # Setting up the right paddle
Lpaddle = Paddle(screen, 'left')     # Setting up the left paddle

def right_paddle_up():
    Rpaddle.up(screen)

def right_paddle_down():
    Rpaddle.down(screen)

def left_paddle_up():
    Lpaddle.up(screen)

def left_paddle_down():
    Lpaddle.down(screen)


screen.listen()
screen.onkey(right_paddle_up, 'Up')        # Setting up the right paddle's up key
screen.onkey(right_paddle_down, 'Down')   # Setting up the right paddle's down key
screen.onkey(left_paddle_up, 'w')        # Setting up the left paddle's up key
screen.onkey(left_paddle_down, 's')      # Setting up the left paddle's down key


screen.exitonclick()