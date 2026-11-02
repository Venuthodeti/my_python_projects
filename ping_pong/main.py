from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
screen = Screen()
score=ScoreBoard()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
paddle=Paddle()
paddle_1=Paddle()
paddle_1.goto(350, 0)
ball=Ball()
screen.listen()
screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
game_is_on=True
x=0.1
while game_is_on:

    time.sleep(x)

    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.xcor() < -320 and ball.distance(paddle) < 50:
        x*=0.9
        ball.bounce_x()
    if ball.xcor() > 320 and ball.distance(paddle_1) < 50:
        x*=0.9
        ball.bounce_x()
    if ball.xcor() < -400 :
        x=0.1
        ball.goto(0, 0)
        ball.bounce_x()
        score.increase_score_1()
        score.display_score()
    if  ball.xcor() > 400:
        x=0.1
        ball.goto(0, 0)
        ball.bounce_x()
        score.increase_score_2()
        score.display_score()

    screen.update()
screen.exitonclick()