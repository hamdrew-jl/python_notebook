# 02 Turtle Racing Game

* Build  a turtle race
* Know the concept of state and instances
* Multiple turtles to join the game.

## Objectives
* Start a popup that asks us to bet which turtle will win the race and choose a color.
* Turtles lined up in the starting position
* Each turtle starts to make random steps toward the right edge of the screen.
* Once a turtle reaches the right edge of the screen, the turtle will be the winner
* Output the result. Let us know if we win or lose and the winner's color.

## Tutorial version
  
![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/c2b6081f-da6d-4c53-b757-7ab294522e06)


## Self-practice

I practice on this program a bit

* First: (Draw tracer need more time so I deleted in the lastest version)

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/557286d8-a601-4801-8024-c92536894407)

* Second:
  
![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/90e632f5-ead3-4b15-b2fa-26812197e819)



## Steps
01 basic code
*  note: We can change the background color and add athletic track to make game more fun.
*  also use turtle.write()method could write word in the game
  
```python
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# bring up popup for user bet
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()

# go to the start of the line
# create six turtles with rainbow color
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
y_position = [-150, -90, -30, 30, 90, 150]
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

```

  
### 02 Add cover

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/cf55760a-adb1-49bf-bd4f-1254be3ddd94)


```python
# title
director = t.Turtle()
director.hideturtle()
director.home()
director.penup()
director.write("Turtle Race", align="center",  font=("Arial", 40, "bold"))
screen.bgcolor("gainsboro")
time.sleep(1)
director.goto(0, -150)
director.write("Color Choose: red/ orange/ yellow/ green/ cyan/ blue/ purple", align="center",  font=("Arial", 15, "bold"))

```
### 02 Change the background color

```python
screen.bgcolor("dark sea green")

```
### 03 Add time delay after popup

```python
director.write("Let's race! ", align="center",  font=("Arial", 40, "bold"))
screen.clear()
time.sleep(1)
```
### 04 Add start line

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/125817b0-97e3-4525-bbc0-e32013faddfd)


```python
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
```

### 05 Add finish flag
* Method 1
  
![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/e740db8f-09aa-496f-9ee5-2627f200891e)

  
```python
def finish_flag():
    """create finish flag"""
    flag = Turtle("square")
    flag.penup()
    flag.speed("fastest")
    x = 200
    y = 180

    for i in range(9):
        flag.goto(x, y)
        flag.stamp()
        x += 20
        y -= 20
        flag.goto(x, y)
        flag.stamp()
        x -= 20
        y -= 20
        flag.goto(x, y)
        flag.stamp()

```
* Method 2
  
  ![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/4db36126-8253-42fa-96f3-40dd49207426)
  
```python
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
```
  
### 06 Add final result show on the screen

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/16c259c1-2ae8-4aea-8b0c-f37fa96d1aef)


```python
director.goto(0, 0)
director.write("The winner is: ", align="center", font=("Arial", 30, "bold"))
turtle_l.stamp()
turtle_l.goto(0, -50)
turtle_l.shapesize(2)

```
if player didn't guess the color or cancel the popup, the screen will show 'Bye'


![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/1c98223f-0ece-49c7-b836-794c86da39d9)

```python

else:
    director.home()
    director.write("Bye", align="center", font=("Arial", 40, "bold"))
```



### 07 Add athletic track (need to be optimized)

```python
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
```

### Full code
```python
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
```
