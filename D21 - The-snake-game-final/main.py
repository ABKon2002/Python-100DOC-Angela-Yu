from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

screen = Screen()
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)    # To get the fluid movement of the snake.

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.ding_ding()
    
    # Detect collision with wall
    if snake.head.xcor() > 345 or snake.head.xcor() < -345 or snake.head.ycor() > 345 or snake.head.ycor() < -345:
        scoreboard.game_over()
        turn_on = False

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            turn_on = False

screen.exitonclick()
