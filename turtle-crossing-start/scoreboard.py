from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-230,250 )
        self.write(f"score={self.score}", align="center", font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"score={self.score}", align="center", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write("GAME OVER", align="center", font=("courier", 50, "bold"))

