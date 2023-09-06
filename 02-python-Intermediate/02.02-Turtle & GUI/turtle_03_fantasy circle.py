from turtle import Turtle, Screen
import random
import turtle as t

# set color mode, or that will be string for default setting
t.colormode(255)
turtle = Turtle()


def randomcolor():
    """set a random RGB color tuple, return r,g,b"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size):
    for i in range(int(360/size)):
        turtle.circle(100)
        turtle.color(randomcolor())
        print(turtle.heading())

        # change the direction slight each time when draw circle
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size)


# change the speed
turtle.speed('fastest')

turtle.circle(100)

draw_spirograph(10)


# Output
screen = Screen()
screen.exitonclick()
