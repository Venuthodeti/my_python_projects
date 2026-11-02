import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car=[]
    def create_car(self):
        rand=random.randint(0,6)
        if rand ==1:
            car=Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300,random.randint(-250,250))
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.append(car)

    def move_cars(self):
        for car in self.car:
            car.backward(MOVE_INCREMENT)

