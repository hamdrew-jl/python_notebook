# Method 1
"""interact with user"""


from turtle import Turtle, Screen, colormode
import random
colormode(255)
turtle = Turtle()


def randomcolor():
    """set a random RGB color tuple, return r,g,b"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def circle_graphic(size_c, angle_c):
    for c in range(loop_number):
        turtle.color(randomcolor())
        turtle.circle(size_c)
        turtle.left(angle_c)


angle = int(input("How much do you want the turtle to turn? (1 to 180)"))
size = int(input("How large do you want the circle?"))
loop_number = int(360 / angle)

# change the speed
turtle.speed("fastest")

circle_graphic(size, angle)

# Output
screen = Screen()
screen.exitonclick()


# _______________________________________________________________________________
# Method 2
 """use heading()"""
# from turtle import Turtle, Screen, colormode
# import random


# colormode(255)
# turtle = Turtle()


# def randomcolor():
#     """set a random RGB color tuple, return r,g,b"""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b


# def draw_spirograph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         turtle.circle(100)
#         turtle.color(randomcolor())
#         print(turtle.heading())

#         # change the direction slight each time when draw circle
#         current_heading = turtle.heading()
#         turtle.setheading(current_heading + size_of_gap)


# # change the speed
# turtle.speed('fastest')

# # turtle.circle(100)
# draw_spirograph(5)

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
#         turtle.left(360 / num)


# turtle.speed("fastest")

# draw_circlegraph(20)

# screen = Screen()
# screen.exitonclick()
