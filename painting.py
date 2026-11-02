import random
import turtle as t

a = t.Turtle()
b = t.Screen()
t.colormode(255)
a.speed("fastest")

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
a.penup()
a.left(220)
a.forward(400)
a.left(140)
a.pendown()
for i in range(13):
    for i in range(13):
        a.dot(20, rand_color())
        a.penup()
        a.forward(50)
        a.pendown()
        if (i==12):
            a.penup()
            a.left(90)
            a.forward(40)
            a.left(90)
            a.forward(650)
            a.left(180)










b.exitonclick()
