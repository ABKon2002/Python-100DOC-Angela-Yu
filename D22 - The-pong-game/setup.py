from turtle import Turtle, Screen

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

def setup_screen():
    screen = Screen()
    screen.title("Pong")
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.tracer(0)
    return screen, SCREEN_WIDTH, SCREEN_HEIGHT

def setup_midline(screen):
    midline = Turtle()
    midline.hideturtle()
    midline.penup()
    midline.speed(0)
    midline.goto(0, 350)
    midline.pendown()
    midline.right(90)
    midline.pencolor('white')
    while midline.ycor() >= -350:
        midline.forward(15)
        midline.penup()
        midline.forward(15)
        midline.pendown()
    screen.update()
    return midline