from turtle import *
from turtle_movement import Turtle_movement
from cars_Manager import *
from scoreboard import Scoreboard
import time


# Create a turtle object
tim = Turtle_movement(0, -280)
car_manager = Car_Manager()
scoreboard = Scoreboard()

# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)


# Making the screen listen for key presses
screen.listen()
screen.onkey(tim.go_up, "Up")

# Game is on
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    if tim.ycor() > 280:
        tim.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()
    for car in car_manager.all_cars:
        if car.distance(tim) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()




