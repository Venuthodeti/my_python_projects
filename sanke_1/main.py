from turtle import  Screen
import time
from snnnnn import Snake
from food import Food
from score import Score
score=Score()

screen = Screen()
food=Food()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off animation for manual updates
snake= Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
x=0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(x)
    snake.move()
    if snake.head.distance(food) < 15:#distance is a predefined function in turtle syntax is y.distance(x)
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300:
        snake.x_axis()
    if  snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        snake.y_axis()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            snake.create_snake()




screen.exitonclick()