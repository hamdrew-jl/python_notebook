# Damien Hirst's painting: Anitipyrylazo III
# Crack color in this painting, and use those colors to generate a random canvas of spot paintings
# use package colorgram

# import colorgram

 """use colorgram to extract the color,
 and testing out these colors into new color_list"""
# # rgb_color = []
# # colors = colorgram.extract('damien-hirst-lactulose.jpg', 15)
# #
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.b
# #     b = color.rgb.b
# #     new_color = (r, g, b)
# #     rgb_color.append(new_color)
# #
# # print(rgb_color)

# ---------------------------------------------------------------------------
"""Method 1 goto() method"""
from turtle import Turtle, Screen, colormode
import random

color_list = [ (25, 164, 164), (194, 81, 81), (238, 49, 49), (234, 85, 85),
               (226, 228, 228), (223, 176, 176), (144, 56, 56), (102, 219, 219),
               (206, 29, 29), (20, 132, 132), (214, 90, 90), (239, 50, 50),
               (141, 227, 227), (118, 140, 140), (3, 176, 176), (106, 199, 199),
               (138, 73, 73), (4, 86, 86), (98, 36, 36), (22, 210, 210),
               (232, 184, 184), (175, 221, 221), (29, 95, 95), (233, 161, 161),
               (152, 190, 190), (242, 8, 8), (89, 31, 31)]

colormode(255)
turtle = Turtle()
turtle.hideturtle()
turtle.pinup()
turtle.speed(0)

for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        turtle.goto(x, y)
        turtle.dot(20, random.choice(color_list))

# Output
screen = Screen()
screen.exitonclick()

# ---------------------------------------------------------------------------
"""Method 2  setx/sety()  method"""
# from turtle import Turtle, Screen, colormode
# import random
# color_list = [ (25, 164, 164), (194, 81, 81), (238, 49, 49), (234, 85, 85),
#                (226, 228, 228), (223, 176, 176), (144, 56, 56), (102, 219, 219),
#                (206, 29, 29), (20, 132, 132), (214, 90, 90), (239, 50, 50),
#                (141, 227, 227), (118, 140, 140), (3, 176, 176), (106, 199, 199),
#                (138, 73, 73), (4, 86, 86), (98, 36, 36), (22, 210, 210),
#                (232, 184, 184), (175, 221, 221), (29, 95, 95), (233, 161, 161),
#                (152, 190, 190), (242, 8, 8), (89, 31, 31)]


# colormode(255)
# turtle = Turtle()
# turtle.hideturtle()
# turtle.penup()
# turtle.speed(0)


# def draw_dot(length):
#     """draw dot line horizontally """
#     for _ in range(length):
#         turtle.dot(20, random.choice(color_list))
#         turtle.forward(50)
#     turtle.setx(turtle.xcor() - (50 * length))
#     turtle.sety(turtle.ycor() + 50)


# def draw_painting(height, width):
#     """add vertical movement and print the painting"""
#     turtle.setx(-25 * height)
#     turtle.sety(-25 * width)
#     for _ in range(height):
#         draw_dot(width)


# draw_painting(10, 10)

# # Output
# screen = Screen()
# screen.exitonclick()
