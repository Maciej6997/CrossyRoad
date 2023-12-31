from turtle import Turtle
from random import randint,choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.increment = 0



    def add_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.setheading(180)
        new_car.goto(280,randint(-250,250))
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + self.increment)