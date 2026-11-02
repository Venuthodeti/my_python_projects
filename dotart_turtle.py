import random
import turtle as t

a = t.Turtle()
b = t.Screen()
t.colormode(255)
a.speed("fastest")
a.penup()
a.goto(-b.window_width() // 2, -b.window_height() // 2)  # Bottom-left corner
a.pendown()

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(200):
    a.dot(10, rand_color())
    a.penup()
    a.forward(50)
    a.pendown()

b.exitonclick()
