import turtle as t
import time
import random

# screen setting
is_going_on = False
screen = t.Screen()
screen.title("Turtle Race")
screen.setup(800, 500)

director = t.Turtle()
director.hideturtle()
director.home()
director.penup()
director.write("Turtle Race", align="center",  font=("Arial", 40, "bold"))
screen.bgcolor("gainsboro")
time.sleep(1)
director.goto(0, -150)
director.write("Color Choose: red/ orange/ yellow/ green/ cyan/ blue/ purple", align="center",  font=("Arial", 15, "bold"))

# popup
text_guess = t.textinput("Make your bet", "Which turtle will win? Enter a color: ")

director.write("Let's race! ", align="center",  font=("Arial", 40, "bold"))
screen.clear()
time.sleep(1)


def start_line():
    start = t.Turtle()
    start.speed(0)
    start.penup()
    start.hideturtle()
    start.goto(-250, 180)
    start.setheading(270)
    start.pendown()
    start.pensize(3)
    start.forward(350)


def final_flag():

    for i in range(2):
        flag = t.Turtle("square")
        flag.speed(0)
        flag.penup()
        flag.hideturtle()
        flag.color("black")
        flag.goto(350, 200)
        flag.setheading(270)
        for y in range(-200, 200, 40):
            flag.stamp()
            flag.forward(40)
        flag.color("white")
        flag.goto(350, 180)
        flag.setheading(270)
        for y in range(-180, 180, 40):
            flag.stamp()
            flag.forward(40)


def multiple_turtles():
    all_turtles = []
    y_position = [-120, -80, -40, 0, 40, 80, 120]
    color = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

    for turtle_index in range(len(y_position)):
        new_turtle = t.Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(color[turtle_index])
        new_turtle.goto(-270, y_position[turtle_index])
        all_turtles.append(new_turtle)
    return all_turtles


if text_guess:
    is_going_on = True

    # background graphic
    screen.bgcolor("dark sea green")

    start_line()
    final_flag()
    all_t = multiple_turtles()
    time.sleep(1)

    while is_going_on:

        for turtle_l in all_t:
            if turtle_l.xcor() > 330:
                is_going_on = False

                director.goto(0, 0)
                director.write("The winner is: ", align="center", font=("Arial", 30, "bold"))
                turtle_l.stamp()
                turtle_l.goto(0, -50)
                turtle_l.shapesize(2)

                if text_guess == turtle_l.color():
                    print(f"You lose. The winner is {turtle_l.pencolor()} turtle.")
                else:
                    print(f"You win. The winner is {turtle_l.pencolor()} turtle.")

            turtle_l.forward(random.randint(2, 15))
else:
    director.home()
    director.write("Bye", align="center", font=("Arial", 40, "bold"))

# Output
screen.exitonclick()
