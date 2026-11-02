from turtle import Turtle,Screen
# import time
#
# turtle = Turtle()
# turtle.penup()
# screen = Screen()
# screen.tracer(0)
# screen.setup(800,600)
# screen.bgcolor("black")
# turtle.color("white")
# turtle.shape("square")
# turtle.shapesize(stretch_wid=1,stretch_len=5)
# turtle.goto(350,0)
# while True:
#     time.sleep(0.1)
#     turtle.back(10)
#     if turtle.xcor() < -450:
#         turtle.goto(450,0)
#     screen.update()
# screen.exitonclick()


class RoadTurtle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x,0)
