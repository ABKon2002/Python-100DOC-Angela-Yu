from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)    # To get the fluid movement of the snake.

# 1. Creating the snake body using 3 different turtle objects.

positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

for position in positions:
    segment = Turtle('square')
    segment.color('white')
    segment.penup()
    segment.goto(position)
    snake_segments.append(segment)

# 2. Moving the snake forward and connecting the segments.
# ** Hint: Update segments in reverse. ** #

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[i - 1].xcor()
        new_y = snake_segments[i - 1].ycor()
        snake_segments[i].goto(new_x, new_y)

    snake_segments[0].forward(20)

# screen.listen()
# screen.onkey(snake_segments[0].left, 'Left')
# screen.onkey(snake_segments[0].right, 'Right')
# screen.onkey(snake_segments[0].up, 'Up')
# screen.onkey(snake_segments[0].down, 'Down')

screen.exitonclick()