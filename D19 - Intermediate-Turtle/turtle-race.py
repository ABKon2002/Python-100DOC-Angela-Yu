from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
screen.bgcolor("light blue")
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color in the rainbow: ").lower()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
y = -150
for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

for turtle in all_turtles:
    turtle.pendown()

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                exit()
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                exit()
        random_distance = random.randint(0, 20)
        turtle.forward(random_distance)

screen.exitonclick()