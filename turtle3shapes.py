import random
import turtle as t
a=t.Turtle()
b=t.Screen()
angles=[90,180,270,0]
colors=["red","yellow","brown","blue","pink","violet","black","orange"]
a.pensize(15)

while 2>1:
    a.color(random.choice(colors))
    a.forward(30)
    a.left(random.choice(angles))
    

    
b.exitonclick()