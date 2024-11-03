from turtle import Turtle

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
OFFSET = 25    # Distance from the paddle and the wall
MOVE_DISTANCE = 50

class Paddle:
    def __init__(self, screen, side):
        if side == 'right':
            paddle = Turtle('square')
            paddle.color('white')
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.penup()
            paddle.goto((SCREEN_WIDTH / 2) - OFFSET, 0)
            self.paddle = paddle
        elif side == 'left':
            paddle = Turtle('square')
            paddle.color('white')
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.penup()
            paddle.goto(-((SCREEN_WIDTH / 2) - OFFSET), 0)
            self.paddle = paddle
        
        screen.update()
    
    def up(self, screen):
        # Move the paddle up if it is not touching the top wall
        if self.paddle.ycor() < ((SCREEN_HEIGHT / 2) - OFFSET) - 45:
            new_y = self.paddle.ycor() + MOVE_DISTANCE
            self.paddle.sety(new_y)
            screen.update()
    
    def down(self, screen):
        # Move the paddle down if it is not touching the bottom wall
        if self.paddle.ycor() > -((SCREEN_HEIGHT / 2) + OFFSET) + 85:
            new_y = self.paddle.ycor() - MOVE_DISTANCE
            self.paddle.sety(new_y)
            screen.update()

