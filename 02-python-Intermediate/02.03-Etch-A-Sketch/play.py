from turtle import Turtle, Screen, colormode
import random
import turtle as t

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
y_position = [-150, -90, -30, 30, 90, 150]
screen.bgcolor("dark sea green")


def athletic_track():
    """create athletic track"""
    track = Turtle()
    track.speed(0)
    for y in range(-180, 210, 60):
        for x in range(-280, 310, 60):
            track.color("white smoke")
            track.pensize(10)
            track.penup()
            track.goto(x, y)
            track.pendown()
            track.forward(100)


# bring up popup for user bet
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()

athletic_track()

# title
t.penup()
t.hideturtle()
t.goto(-80, 175)
t.write("Welcome to The Race!", font=("Arialblack", 10))

# colors = ['firebrick', 'dark orange', 'gold', 'dodger blue', 'green yellow', 'slate blue']
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

# go to the start of the line, create six turtles with rainbow color
all_turtles = []
for index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-240, y=y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            # print(f"The winner in this race is {turtle.color()}")
            if user_bet == turtle.color():
                print(f"You win! The winner is [{turtle.pencolor()}] turtle.")
            else:
                print(f"You lose! The winner is [{turtle.pencolor()}]turtle.")
        # random movement, random step distance
        turtle.forward(random.randint(0, 10))


screen.exitonclick()