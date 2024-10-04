from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating objects in the aimation
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Moving the snake
screen.listen()
screen.onkey(snake.go_left, "a")
screen.onkey(snake.go_down, "s")
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280  or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()  

    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
screen.exitonclick()