import turtle as t
import pandas as pd
turtle = t.Turtle()
screen=t.Screen()
image="india.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("Book3.csv")
score=0
while score<=27:
    ans=screen.textinput(title=f'Score: {score}/28',prompt='Enter your answer').title()
    if ans=="Exit":
        break
    for i in range (len(data["states"])):
        if data["states"][i]==ans:
            tu=t.Turtle()
            tu.color("black")
            tu.penup()
            tu.hideturtle()

            tu.goto(data["x"][i],data["y"][i])
            tu.write(ans, font=("Arial", 10, "bold"))
            score+=1



