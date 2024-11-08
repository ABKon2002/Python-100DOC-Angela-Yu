from turtle import Turtle
import time

X_MOVEMENT = 5
Y_MOVEMENT = 5
SPEED_INCREASE = 0.20   # 25 % increase in speed
START_SPEED = 3

class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(0.5, 0.5)
        self.color("white")
        self.goto(0, 0)
        self.move_speed = START_SPEED
        self.x_move = X_MOVEMENT
        self.y_move = Y_MOVEMENT
        screen.update()

    def move(self):
        new_x = self.xcor() + (self.x_move * self.move_speed)
        new_y = self.ycor() + (self.y_move * self.move_speed)
        self.goto(new_x, new_y)
        self.pos = (new_x, new_y)  # Update the pos variable after moving the ball
    
    def reset_position(self):
        time.sleep(1)
        self.goto(0, 0)
        self.move_speed = START_SPEED
        self.bounce_x()
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed = self.move_speed + (self.move_speed * SPEED_INCREASE)