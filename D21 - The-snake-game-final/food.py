from turtle import Turtle
import random

FOOD_COLOR = "blue"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-330, 310)
        random_y = random.randint(-330, 310)
        self.goto(random_x, random_y)