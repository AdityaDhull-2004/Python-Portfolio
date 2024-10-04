from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, 200)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):

        self.write(f"{self.score}", align="center", font=("Courier", 80, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.write(f"{self.score}", align="center", font=("Courier", 80, "normal"))

    def winner(self):
        self.write(f"Player {self.score} Wins", align="center", font=("Courier", 80, "normal"))
    
    