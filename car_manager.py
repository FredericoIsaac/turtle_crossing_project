from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars_list = []
        self.create_car()
        self.increase_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(0, 6) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            self.cars_list.append(new_car)

    def move(self):
        for car in self.cars_list:
            car.backward(self.increase_speed)

    def new_level(self):
        self.increase_speed += MOVE_INCREMENT
