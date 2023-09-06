# Draw a Random walk.
# What is Random walk. go to link:  https://en.wikipedia.org/wiki/Random_walk
# Require: 1. random walk.  2.  each time it walks, it's going to pick a different color.


from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)
turtle = Turtle()

# color library, for some reason, it cannot use colormode method.
# colors = ["red", "yellow", "pink", "brown", "purple", "SeaGreen", "green", "orange", "blue"]

# set a random direction
direction = [0, 90, 180, 270]


# random color
def randomcolor():
    """set a random RGB color tuple, return r,g,b"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# random walk Function
def random_walk():
    turtle.seth(random.choice(direction))
    turtle.color(randomcolor())
    turtle.pensize(10)
    turtle.fd(30)
    turtle.speed("fastest")


for i in range(100):
    random_walk()


# Output
screen = Screen()
screen.exitonclick()