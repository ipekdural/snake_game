from turtle import Turtle
scores=[]
class HighestScore(Turtle):
    def __init__(self):
        super().__init__()


    def append(self,score):
        scores.append(score)
    def highest_score(self):
        return max(scores)
    def update_scoreboard(self):
        highest=self.highest_score()
        self.color("gREEN")
        self.penup()
        self.hideturtle()
        self.goto(50, 260)
        self.write(f"Highest Score:{highest}",align="center",font=("Courier",16,"normal"))


    def write_(self):
        self.clear()
        self.update_scoreboard()