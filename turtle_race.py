import turtle
import random
screen=turtle.Screen()
screen.setup(600,500)
bet=screen.textinput("bet","What color?")
tom=turtle.Turtle()
tom.pensize(10)
tom.penup()
tom.goto(200,-240)
tom.pendown()
tom.left(90)
for i in range(10):
    tom.forward(30)
    tom.penup()
    tom.forward(30)
    tom.pendown()
colors=["red","black","yellow","brown","orange","pink","blue"]
names=[]
for i in range(len(colors)):
    tim=turtle.Turtle()
    tim.color(colors[i])
    tim.shape("turtle")
    names.append(tim)
y=(-210)
for i in range(len(names)):
    names[i].penup()
    names[i].goto(-280,y)
    names[i].pendown()
    y=y+70

if bet:
    game_is_on = True
while game_is_on:
    for i in range(len(names)):
        if names[i].xcor()>200:
            game_is_on=False
            winner=names[i].pencolor()
            if winner==bet:
                print(f"Congratulations! You won!,winning color is {winner}")
            else:
                print(f"Sorry! You lost!,winning color is {winner}")
        names[i].penup()
        names[i].forward(random.randint(1,10))


screen.exitonclick()
