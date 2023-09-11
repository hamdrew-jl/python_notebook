# Tom & Jerry


![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/27137836-c10b-42f3-937a-5c2ec4b8d2ab)

![tom1](https://github.com/hamdrew-jl/python_notebook/assets/141601957/604ffc41-7cb2-4b03-9662-145562c8ada3)

![jerry2](https://github.com/hamdrew-jl/python_notebook/assets/141601957/ba4a9f44-d3ba-4772-83c8-fe6563dc8799)


```python
import turtle
import time
import random

screen = turtle.Screen()
screen.title("Tom & Jerry")
screen.register_shape("tom1.gif")
screen.register_shape("jerry2.gif")

# listen
screen.listen()

director = turtle.Turtle()
director.hideturtle()
director.color("black")
director.penup()
director.home()
director.write("Tom & Jerry", align="center", font=("Arial", 50, "bold"))
director.goto(0, -50)
director.write("Game begin in few seconds....", align="center", font=("Arial", 20, "bold"))
director.goto(0, -100)
director.write("Keyboard control Jerry (↑ ↓ ← →)", align="center", font=("Arial", 20, "bold"))
time.sleep(1)

# counting down
director.clear()
director.write("3", align="center", font=("Arial", 50, "bold"))
time.sleep(1)
director.clear()
director.write("2", align="center", font=("Arial", 50, "bold"))
time.sleep(1)
director.clear()
director.write("1", align="center", font=("Arial", 50, "bold"))
time.sleep(1)
director.clear()
start = time.time()

# Create Tom & Jerry Object
tom = turtle.Turtle()
tom.shape("tom1.gif")
tom.penup()
tom.goto(random.randint(-200, 200), random.randint(-200, 200))
tom.penup()

jerry = turtle.Turtle()
jerry.shape("jerry2.gif")
jerry.speed(0)
jerry.penup()
jerry.goto(random.randint(-200, 200), random.randint(-200, 200))
jerry.color("brown")

# Movement
def up():
    jerry.setheading(90)
    jerry.forward(20)


def down():
    jerry.setheading(270)
    jerry.forward(20)


def left():
    jerry.setheading(180)
    jerry.forward(20)


def right():
    jerry.setheading(0)
    jerry.forward(20)


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# Prepare the game
is_go_on = True
while is_go_on:
    tom.setheading(tom.towards(jerry))
    tom.forward(5)
    if tom.distance(jerry) < 10:
        end = time.time()
        screen.clear()
        jerry.goto(0, 0)
        jerry.write("Game Over", align="center", font=("Arial", 50, "bold"))
        jerry.goto(0, -50)
        jerry.write("You stand {:.1f}s".format(end-start), align="center", font=("Arial", 20, "bold"))
        tom.penup()
        tom.goto(-30, -140)
        tom.stamp()
        turtle.mainloop()
        is_go_on = False

# Output
screen.exitonclick()
```
