from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_1 = 0
        self.score_2 = 0
        self.goto(0, 260)
        self.write(f"{self.score_2}     -     {self.score_1}", align="center", font=("Arial", 20, "bold"))



    def increase_score_1(self):
        self.score_1 += 1

    def increase_score_2(self):
        self.score_2 += 1


    def display_score(self):
        self.clear()
        self.goto(0, 260)
        self.color("white")
        self.write(f" {self.score_2}     -     {self.score_1}", align="center", font=("Arial", 20, "bold"))


