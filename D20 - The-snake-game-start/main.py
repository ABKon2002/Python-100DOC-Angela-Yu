from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)    # To get the fluid movement of the snake.

snake = Snake()

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

screen.exitonclick()