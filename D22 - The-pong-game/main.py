from setup import setup_screen, setup_midline
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen, SCREEN_WIDTH, SCREEN_HEIGHT = setup_screen()
midline = setup_midline(screen)

scoreboard = Scoreboard()

Rpaddle = Paddle(screen, 'right')    # Setting up the right paddle
Lpaddle = Paddle(screen, 'left')     # Setting up the left paddle

ball = Ball(screen)

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

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    # Detecting collision with the wall
    if ball.ycor() > (SCREEN_HEIGHT / 2) - 10 or ball.ycor() < -(SCREEN_HEIGHT / 2) + 10:
        ball.bounce_y()
    
    # Detecting collision with the paddles
    if ball.distance(Rpaddle) < 50 and ball.xcor() > (SCREEN_WIDTH / 2) - 50:
        ball.bounce_x()
    elif ball.distance(Lpaddle) < 50 and ball.xcor() < -(SCREEN_WIDTH / 2) + 50:
        ball.bounce_x()
    
    # Detecting paddle misses
    if ball.xcor() > (SCREEN_WIDTH / 2) + 30:
        game_on = scoreboard.ding_ding_right()
        ball.reset_position()
    elif ball.xcor() < -(SCREEN_WIDTH / 2) - 30:
        game_on = scoreboard.ding_ding_left()
        ball.reset_position()


screen.exitonclick()