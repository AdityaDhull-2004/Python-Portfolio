from turtle import *
with open("My_File.txt") as file:
    contents = file.read()
    a = int(contents)

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.high_score = a
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        if a < self.high_score:
            with open("My_File.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        file.close()
        self.score = 0
        self.clear()
        self.update_scoreboard()
        
    #def game_over(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))