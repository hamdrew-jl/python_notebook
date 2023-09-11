from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-50, 200)
        self.write(f"{self.score_l}", align=ALIGNMENT, font=FONT)
        self.goto(50, 200)
        self.write(f"{self.score_r}", align=ALIGNMENT, font=FONT)

    def add_score_l(self):
        self.clear()
        self.score_l += 1
        self.update_score()

    def add_score_r(self):
        self.clear()
        self.score_r += 1
        self.update_score()


    # TODO finish the winner     
    # def winner(self):
    #     if self.score_r == 11:
    #         self.write("The winner is Right", align=ALIGNMENT, font=FONT)
    #     if self.score_l == 11:
    #         self.write("The winner is Left", align=ALIGNMENT, font=FONT)
