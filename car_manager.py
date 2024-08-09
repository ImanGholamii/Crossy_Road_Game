from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        car = Turtle()
        car.penup()
        car.color(choice(COLORS))
        car.shape("square")
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setposition(x=270, y=randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

