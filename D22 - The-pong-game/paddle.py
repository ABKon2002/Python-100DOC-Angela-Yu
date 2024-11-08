from turtle import Turtle

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
OFFSET = 25    # Distance from the paddle and the wall
MOVE_DISTANCE = 50

class Paddle(Turtle):
    def __init__(self, screen, side):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if side == 'right':
            self.goto((SCREEN_WIDTH / 2) - OFFSET, 0)
        elif side == 'left':
            self.goto(-((SCREEN_WIDTH / 2) - OFFSET), 0)
        
        screen.update()
    
    def up(self, screen):
        # Move the paddle up if it is not touching the top wall
        if self.ycor() < ((SCREEN_HEIGHT / 2) - OFFSET) - 45:
            new_y = self.ycor() + MOVE_DISTANCE
            self.sety(new_y)
            screen.update()
    
    def down(self, screen):
        # Move the paddle down if it is not touching the bottom wall
        if self.ycor() > -((SCREEN_HEIGHT / 2) + OFFSET) + 85:
            new_y = self.ycor() - MOVE_DISTANCE
            self.sety(new_y)
            screen.update()

