from turtle import Turtle,Screen

screen=Screen()
screen.bgcolor("black")
def up():
    for i in range(3):
        angle = new[i].heading()
        if (int(angle) == 0):
            new[i].left(90)
        elif (int(angle) == 180):
            new[i].right(90)
        elif (int(angle) == 90):
            pass
        elif (int(angle) == 270):
            new[i].left(180)
        new[i].forward(10)


def down():
    for i in range(3):
        angle = new[i].heading()
        if (int(angle) == 180):
            new[i].left(90)
        elif (int(angle) == 270):
            pass
        elif (int(angle)==0):
            new[i].right(90)
        elif(int(angle) == 90):
            new[i].right(180)
        new[i].forward(10)
def right():
    for i in range(3):
        angle = new[i].heading()
        if (int(angle) == 0):
            pass
        elif (int(angle) == 90):
            new[i].right(90)
        elif (int(angle)==180):
            new[i].right(180)
        elif(int(angle) == 270):
            new[i].left(90)
        new[i].forward(10)
def left():
    for i in range(3):
        angle = new[i].heading()
        if (int(angle) == 0):
            new[i].left(180)
        elif (int(angle) == 90):
            new[i].left(90)
        elif (int(angle)==180):
            pass
        elif(int(angle) == 270):
            new[i].right(90)
        new[i].forward(10)
def penup():
    new[i].penup()
def pendown():
    new[i].pendown()

new=[]
x=0
for i in range (3):
    jai=Turtle("square")
    jai.penup()
    jai.color("white")
    jai.goto(x,0)

    new.append(jai)
    x-=20



screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Left", fun=left)
screen.onkey(key="u", fun=penup)
screen.onkey(key="d", fun=pendown)
screen.exitonclick()
screen.mainloop()



