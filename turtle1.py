from turtle import Turtle, Screen

kittu_the_king = Turtle()
kittu_the_king.shape("classic")
kittu_the_king.color("red")
kittu_the_king.pencolor("red")
kittu_the_king.forward(100)
kittu_the_king.left(90)
kittu_the_king.forward(100)
kittu_the_king.left(90)
kittu_the_king.forward(100)
kittu_the_king.left(90)
kittu_the_king.forward(100)
kittu_the_king.left(135)
kittu_the_king.forward(141.4)
for i in range(360):
    kittu_the_king.forward(1)
    kittu_the_king.left(1)
for i in range(6):
    kittu_the_king.forward(100)
    kittu_the_king.left(60)
for i in range(3):
    kittu_the_king.forward(100)
    kittu_the_king.left(120)
# Keeps the screen open until you click on it
Screen().exitonclick()
