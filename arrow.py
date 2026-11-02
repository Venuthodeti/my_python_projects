import turtle

screen = turtle.Screen()
tim = turtle.Turtle()



def up():
    angle = tim.heading()
    if (int(angle) == 0):
        tim.left(90)
    elif (int(angle) == 180):
        tim.right(90)
    elif (int(angle) == 90):
        pass
    elif (int(angle) == 270):
        tim.left(180)
    tim.forward(10)


def down():
    angle = tim.heading()
    if (int(angle) == 180):
        tim.left(90)
    elif (int(angle) == 270):
        pass
    elif (int(angle)==0):
        tim.right(90)
    elif(int(angle) == 90):
        tim.right(180)
    tim.forward(10)
def right():
    angle = tim.heading()
    if (int(angle) == 0):
        pass
    elif (int(angle) == 90):
        tim.right(90)
    elif (int(angle)==180):
        tim.right(180)
    elif(int(angle) == 270):
        tim.left(90)
    tim.forward(10)
def left():
    angle = tim.heading()
    if (int(angle) == 0):
        tim.left(180)
    elif (int(angle) == 90):
        tim.left(90)
    elif (int(angle)==180):
        pass
    elif(int(angle) == 270):
        tim.right(90)
    tim.forward(10)
def penup():
    tim.penup()
def pendown():
    tim.pendown()


screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Left", fun=left)
screen.onkey(key="u", fun=penup)
screen.onkey(key="d", fun=pendown)
screen.exitonclick()
# import turtle
#
# screen = turtle.Screen()
# tim = turtle.Turtle()
#
# def up():
#     angle = tim.heading()
#     if int(angle) == 0:        # Facing East
#         tim.left(90)
#     elif int(angle) == 90:     # Facing North
#         pass
#     elif int(angle) == 180:    # Facing West
#         tim.right(90)
#     elif int(angle) == 270:    # Facing South
#         tim.left(180)
#     tim.forward(10)
#
# def down():
#     angle = tim.heading()
#     if int(angle) == 180:      # Facing West
#         tim.left(90)
#     elif int(angle) == 90:     # Facing North
#         tim.right(180)
#     elif int(angle) == 0:      # Facing East
#         tim.right(90)
#     elif int(angle) == 270:    # Facing South
#         pass
#     tim.forward(10)
#
# screen.listen()
# screen.onkey(key="Up", fun=up)
# screen.onkey(key="Down", fun=down)
# screen.exitonclick()
