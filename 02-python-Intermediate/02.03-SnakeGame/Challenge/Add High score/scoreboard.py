from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 10, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score {self.high_score} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0  # be aware the location
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
