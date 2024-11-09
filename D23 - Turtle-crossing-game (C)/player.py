from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        if self.ycor() > self.finish_line:
            return True
        else:
            return False
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
