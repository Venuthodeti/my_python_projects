from turtle import Turtle,Screen
import time
turtle=Turtle()
screen=Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
turtle.shape("circle")

turtle.color("white")
turtle.penup()
turtle.goto(00,00)
screen.update()
screen.exitonclick()
while True:
    time.sleep(0.1)

    new_x=turtle.xcor()+10
    new_y=turtle.ycor()+10
    turtle.goto(new_x,new_y)
    screen.update()