from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.x_move = STARTING_MOVE_DISTANCE
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.setheading(180)
        self.color(choice(COLORS))
        self.goto(300, randint(-250, 250))
    
    def move(self):
        self.forward(self.x_move)
        if self.xcor() < -340:
            return True
            


class CarManager:
    def __init__(self):
        self.level = 0
        self.difficulty = 'easy'
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.difficulty_chart = {'easy': [1], 'medium': [1, 2], 'hard': [1, 2, 3]}

    def create_car(self, difficulty = 'easy'):
        random_chance = randint(1, 6)
        if random_chance in self.difficulty_chart[self.difficulty]:
            new_car = Car()
            new_car.x_move = self.speed
            self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars:
            passed = car.move()
            if passed:
                self.cars.remove(car)
    
    def level_up(self):
        self.speed = self.speed + self.speed * (MOVE_INCREMENT/10)
        self.level += 1
        if self.level > 7:
            self.difficulty = 'medium'
        elif self.level > 15:
            self.difficulty = 'hard'
