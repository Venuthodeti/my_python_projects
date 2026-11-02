import time
from turtle import Screen,Turtle
from player import Player
import player as p
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")
screen.onkey(player.left_turn,"Left")
screen.onkey(player.right_turn,"Right")
game_is_on = True
x=0.1
while game_is_on:
    time.sleep(x)
    car_manager.create_car()

    car_manager.move_cars()
    for car_s in car_manager.car:
        if car_s.distance(player) < 40:
            score.game_over()
            game_is_on = False




    if player.ycor() > 280:
        player.goto(p.STARTING_POSITION)
        score.increase_score()
        x*=0.9


    screen.update()
screen.exitonclick()