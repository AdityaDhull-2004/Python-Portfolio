from turtle import *
position = 0
y = -280

class Turtle_movement(Turtle):
    
    def __init__(self, position, y):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto(position, y)
        self.setheading(90)

    def go_up(self):
            new_y = self.ycor() + 10
            self.goto(self.xcor(), new_y)

    def go_down(self):
            new_y = self.ycor() - 10
            self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(position, y)