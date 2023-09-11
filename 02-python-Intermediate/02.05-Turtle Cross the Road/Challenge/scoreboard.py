from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

    def level_up(self):
        self.clear()
        self.score += 1
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game over", align="center", font=FONT)
