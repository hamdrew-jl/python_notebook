from turtle import Turtle


LIMIT_NUM = 265
MOVE_SPEED = 40
PADDLE_LENGTH = 5


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(PADDLE_LENGTH, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < LIMIT_NUM - MOVE_SPEED:
            new_y = self.ycor() + MOVE_SPEED
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -(LIMIT_NUM - MOVE_SPEED):
            new_y = self.ycor() - MOVE_SPEED
            self.goto(self.xcor(), new_y)
