import random
import turtle as t
a=t.Turtle()
b=t.Screen()
t.colormode(255)
a.speed("fastest")

def rand_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    rgb=(r,g,b)
    return rgb
    


for i in range (36*2):
    a.color(rand_color())
    a.circle(100)
    a.left(5)
b.exitonclick()