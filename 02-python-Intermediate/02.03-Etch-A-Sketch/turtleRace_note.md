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
  
![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/f0c139ec-e094-49ea-bc26-cac588333187)

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/c48357f1-135f-4b93-8925-473d828d6c73)

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/8ac7e66b-eb82-4e95-90d9-16be871827ff)



## Steps
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
* note: We can change the background color and add athletic track to make game more fun!
* also use turtle.write()method could write word in the game
  
### 01 Add title

```python
# title
t.penup()
t.hideturtle()
t.goto(-80, 175)
t.write("Welcome to The Race!", font=("Arialblack", 10))

```
### 02 Change the background color

```python
screen.bgcolor("dark sea green")

```
### 03 Add finish flag

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

### 04 Add athletic track (need to be optimized)

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
