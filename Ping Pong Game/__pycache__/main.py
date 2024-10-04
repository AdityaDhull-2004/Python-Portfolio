from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Creating the screen
screen = Screen()
screen.title("Pong")
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

# Creating the paddles
right_paddle = Paddle(370, 0)
left_paddle = Paddle(-370, 0)

# Creating the ball
c_ball = Ball()


# Make the screen listen for events
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if c_ball.ycor() > 280 or c_ball.ycor() < -280:
        c_ball.bounce_y()
    if c_ball.xcor() > 370 or c_ball.xcor() < -370:
        break
    if c_ball.distance(right_paddle) < 70 and c_ball.xcor() > 350 or c_ball.distance(left_paddle) < 70 and c_ball.xcor() < -350:
        c_ball.bounce_x()
    
        

    c_ball.move()
    
screen.clear()
screen.title("Game Over")
screen.exitonclick()