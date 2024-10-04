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

# Creating the scoreboard
l_scoreboard = Scoreboard(-100)
r_scoreboard = Scoreboard(100)


# Make the screen listen for events
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    c_ball.move()
    if c_ball.ycor() > 280 or c_ball.ycor() < -280:
        c_ball.bounce_y()

        
    if c_ball.xcor() > 370:
        c_ball.reset_position()
        l_scoreboard.increase_score()
        if l_scoreboard.score == 10 and r_scoreboard.score < 10:
            time.sleep(3)
            l_scoreboard.winner()
            game_is_on = False

    if c_ball.xcor() < -370:
        c_ball.reset_position()
        r_scoreboard.increase_score()
        if r_scoreboard.score == 10 and l_scoreboard.score < 10:
            time.sleep(3)
            r_scoreboard.winner()
            game_is_on = False

    if c_ball.distance(right_paddle) < 70 and c_ball.xcor() > 350 or c_ball.distance(left_paddle) < 70 and c_ball.xcor() < -350:
        c_ball.bounce_x()

screen.write("Game Over", align="center", font=("Courier", 24, "normal"))
screen.exitonclick()