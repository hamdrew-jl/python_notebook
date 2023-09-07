# Method 1  
"""interact with user"""
from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
colormode(255)
mathew_the_tortuga.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


turn = int(input("How much do you want the turtle to turn? (1 to 180)"))
size_of_circle = int(input("How large do you want the circle? "))
range_of_loop = int(360 / turn)

for i in range(range_of_loop):
    mathew_the_tortuga.color(random_color())
    mathew_the_tortuga.circle(size_of_circle)
    mathew_the_tortuga.right(turn)

screen = Screen()
screen.exitonclick()


# _______________________________________________________________________________
# Method 2  
"""use headng()"""
# from turtle import Turtle, Screen
# import random
# import turtle as t


# # set colormode, or that will be string for default setting
# t.colormode(255)
# turtle = Turtle()


# def randomcolor():
#     """set a random RGB color tuple, return r,g,b"""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b


# def draw_spirograph(size):
#     for i in range(int(360/size)):
#         turtle.circle(100)
#         turtle.color(randomcolor())
#         print(turtle.heading())

#         # change the direction slight each time when draw circle
#         current_heading = turtle.heading()
#         turtle.setheading(current_heading + size)


# # change the speed
# turtle.speed('fastest')

# turtle.circle(100)

# draw_spirograph(10)


# # Output
# screen = Screen()
# screen.exitonclick()



# _______________________________________________________________________________
# Method 3
"""Input the number of circles you need to draw"""
# from turtle import Turtle, Screen
# import turtle as t
# import random


# t.colormode(255)
# turtle = Turtle()

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b


# def draw_circlegraph(num):

#     for c in range(num):
#         turtle.color(random_color())
#         turtle.circle(50)
#         turtle.left(360/num)


# turtle.speed("fastest")

# draw_circlegraph(20)


# screen = Screen()
# screen.exitonclick()
