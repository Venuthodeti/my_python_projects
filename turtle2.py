import turtle as t
a=t.Turtle()
b=t.Screen()
for i in range(50):
    a.forward(5)
    a.penup()
    a.forward(5)
    a.pendown()
b.exitonclick()

