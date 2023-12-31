# polygon
from turtle import Turtle, Screen
import random

turtle = Turtle()
color = ["red", "yellow", "pink", "brown", "purple", "SeaGreen", "green", "orange"]
# better to choose colormode to have range of color
# turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255) )
turtle.pensize(2)


def shape_side(num_side):
        for _ in range(num_side):
            turtle.forward(100)
            turtle.right(360/num_side)


for n in range(3, 8):
    turtle.color(random.choice(color))
    shape_side(n)




screen = Screen()
screen.exitonclick()
