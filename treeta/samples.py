from turtle import Turtle,Screen
import time
from treeta.moving_turtle import MovingTurtle
from cars import RoadTurtle
import random

screen = Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")
moving_turtle = MovingTurtle()
speeds=[0.1,0,2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
steps=[10,20,30,40]
x=400
y=-200
carray=[]
for i in range(5):
    car = RoadTurtle(x,y)
    y+=100
    carray.append(car)




screen.listen()
screen.onkey(moving_turtle.up,"Up")
screen.onkey(moving_turtle.down,"Down")
screen.onkey(moving_turtle.left,"Left")
screen.onkey(moving_turtle.right,"Right")
while True:
    for arr in carray:
        time.sleep(random.choice(speeds))
        arr.move()
        if arr.xcor() < -450:
            arr.goto(450,arr.ycor())
        screen.update()
screen.exitonclick()
