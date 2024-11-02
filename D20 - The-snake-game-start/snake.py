from turtle import Turtle

# Constants:
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []

        for position in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.snake_segments.append(segment)
        
        self.head = self.snake_segments[0]
    
    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # Check if the snake is not already facing down
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:  # Check if the snake is not already facing up
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:  # Check if the snake is not already facing right
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:  # Check if the snake is not already facing left
            self.head.setheading(RIGHT)
