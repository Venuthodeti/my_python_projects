from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.high_score = 0
        self.score=0
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score} High score :{self.high_score}", align="center", font=("Arial", 20, "bold"))
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score :{self.high_score}", align="center", font=("Arial", 20, "bold"))


    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score=0
        self.update_score()