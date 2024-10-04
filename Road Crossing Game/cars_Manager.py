from turtle import *
import random
Starting_Move_Distance = 6
Move_Increment = 5

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = 300


r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)



class Car_Manager(Turtle):

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.fillcolor(random.choice(colors))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            y = random.randint(-250, 250)
            new_car.goto(position, y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(Starting_Move_Distance)

    def level_up(self):
        global Starting_Move_Distance
        Starting_Move_Distance += Move_Increment
