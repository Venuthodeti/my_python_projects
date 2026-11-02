from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(-350, 0)
        self.shapesize(5, 1)

    def up(self):
        new_y = self.ycor() + 100
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 100
        self.goto(self.xcor(), new_y)

