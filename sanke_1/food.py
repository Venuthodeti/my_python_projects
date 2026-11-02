from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")

    def refresh(self):
        random_number_x = random.randint(-270,270)
        random_number_y = random.randint(-270,270)
        self.goto(random_number_x,random_number_y)