import turtle
import pandas
turtle_=turtle.Turtle()
screen = turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
score=turtle.Turtle()
score.color("red")
score.hideturtle()
score.penup()
score.goto(200,200)
def score_(x):
    score.clear()
    score.write(f"{x}/50", align="center", font=("Arial", 20, "bold"))
score.hideturtle()
x=0
score_(x)
guessed_states=[]
missed_states=[]
while x<=50:
    ans=screen.textinput(title="guess",prompt="What is your guess of state?").capitalize()
    if ans == "Exit":
        for k in range(0,len(data["state"])):
            if data["state"][k] not in guessed_states:
                missed_states.append(data["state"][k])
        print(missed_states)
        break


    for i in range (len(data["state"])):

        if ans==data["state"][i]:
            guessed_states.append(data["state"][i])
            x+=1
            turtle_ = turtle.Turtle()
            turtle_.penup()
            turtle_.hideturtle()
            turtle_.goto(data["x"][i],data["y"][i])
            score_(x)
            turtle_.write(data["state"][i])



