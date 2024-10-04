from turtle import *

positions = [(0,0), (-20,0), (-40,0)]
X = 20

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
            

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(X)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



        
        