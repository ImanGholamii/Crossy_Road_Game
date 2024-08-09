from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setposition(x=300, y=randint(-250, 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

