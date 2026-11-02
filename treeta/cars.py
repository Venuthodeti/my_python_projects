from turtle import Turtle

class RoadTurtle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(x,y)

    def move(self):
        self.back(10)
    def car_model(self):
        pass