import turtle
from turtle import Turtle, Screen
from random import choice, randint
import colorgram

class Shapes:
    def __init__(self, screen):
        turtle.colormode(255)
        self.pen = Turtle()
        self.pen.shape('turtle')
        self.pen.color("red")
        self.pen.fillcolor("dark turquoise")
        self.pen.pensize(5)
        self.colorPalette = ['medium blue', 'dark blue', 'lime green', 'brown', 'purple', 'deep pink', 'medium violet red', 'orange']
        self.screen = screen

    def dashed_line(self, dashes = 20, dash_length = 10):
        pen = self.pen
        for _ in range(dashes):
            pen.forward(dash_length)
            pen.penup()
            pen.forward(dash_length)
            pen.pendown()
    
    def square(self, length = 350):
        pen = self.pen
        for _ in range(4):
            pen.forward(length)
            pen.left(90)
    
    def spiral(self, length = 50, step = 25, rings = 3):
        pen = self.pen
        for _ in range(rings * 4):
            pen.forward(length)
            pen.left(90)
            length += step
    
    def shape_Art_down(self, start_shape = 3, n = 7, length = 75):
        pen = self.pen
        pen.speed(10)
        pen.color(choice(self.colorPalette))
        for n in range(start_shape, start_shape + n + 1):
            angle = 360 / n
            pen.color(choice(self.colorPalette))
            for _ in range(n):
                pen.forward(length)
                pen.right(angle)
    
    def shape_Art_up(self, start_shape = 3, n = 7, length = 75):
        pen = self.pen
        pen.speed(10)
        pen.color(choice(self.colorPalette))
        for n in range(start_shape, start_shape + n + 1):
            angle = 360 / n
            pen.color(choice(self.colorPalette))
            for _ in range(n):
                pen.forward(length)
                pen.left(angle)
    
    def symetric_shape_art(self, n):
        self.shape_Art_down(n = n)
        self.shape_Art_up(n = n)
    
    def random_color_generator(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

    def random_walk(self, steps = 30):
        pen = self.pen
        pen.shape('classic')
        pen.pensize(15)
        pen.speed(0)
        directions = [0, 90, 180, 270]
        for _ in range(steps):
            pen.color(self.random_color_generator())
            pen.forward(25)
            pen.setheading(choice(directions))
    
    def spirograph(self, n = 25):
        pen = self.pen
        pen.pensize(1)
        pen.speed(0)
        angle = 360 / n
        for _ in range(n):
            pen.color(choice(self.colorPalette))
            self.pen.circle(100)
            self.pen.left(angle)
    
    def generate_color_palette(self, image_path = 'Paintings\hirstPainting.png'):
        colors = colorgram.extract(image_path, 30)
        rgb_colors = []
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            rgb_colors.append(new_color)
        for _ in range(3):    # Popping the white colors associated woth the bg. 
            rgb_colors.pop(0)
        self.colorPalette = rgb_colors
    
    def generate_hirst_spot_painting(self):
        self.pen.shape('classic')
        # Setting coordinate  0,0 to the bottom left corner.
        self.screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())
        pen = self.pen
        pen.hideturtle()
        pen.penup()
        pen.speed(0)
        # Going to an apt coord to get the whole figure in the center of the screen. 
        pen.goto(140, 110)
        
        for _ in range(10):
            for _ in range(10):
                pen.dot(20, choice(self.colorPalette))
                pen.forward(50)
            pen.setheading(90)
            pen.forward(50)
            pen.setheading(180)
            pen.forward(500)
            pen.setheading(0)
    
    def test(self):
        pen = self.pen
        pen.pos()
        print(pen.position())


screen = Screen()
draw = Shapes(screen)
#draw.square(250)
#draw.spiral()
#draw.dashed_line()
# draw.symetric_shape_art(10)
# draw.random_walk(100)
# draw.spirograph(75)
draw.generate_color_palette()
draw.generate_hirst_spot_painting()

screen.exitonclick()
