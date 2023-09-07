# Instances, State and Higher Order Functions

## 01 Challenge: Make an Etch-A-Sketch App

* Object:let the turtle sketch on the canvas
* W = Forward
* S = Backward
* A = Counter_clockwise
* D = Clockwise
* C = Clear drawing

Example:

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/5eeb0368-380d-43f7-a030-84d81437c0a8)

### Steps:
1. Import turtle module.

```python

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

```


2. Set move function to guide turtle.
   

```python

def forward():
    tim.forward(20)


def backward():
    tim.backward(20)


def counter_clockwise():
    tim.left(15)
    tim.forward(20)


def clockwise():
    tim.right(15)
    tim.forward(20)


def clear_drawing():
    tim.clear()

```


* Instead of clear() and home(), use turtle.reset()  instead. It does the same and gives you back to where you started from.
  
```python
    tim.reset()
```


3. Use screen function to show the result.

```python

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

```

## More turtles?
1. Turtle() is a class
2. Objects can have different attributes and can be performing different methods

   ```python
   timmy = Turtle()
   tommy = Turtle()
   
   timmy.color = green
   tommy.color = purple
   
   ```
## 02 Turtle Racing Game
* Build  a turtle race
* Know the concept of state and instances
* Multiple turtles to join the game.

### Objectives
* Start a popup that asks us to bet which turtle will win the race and choose a color.
* Turtles lined up in the starting position
* Each turtle starts to make random steps toward the right edge of the screen.
* Once a turtle reaches the right edge of the screen, the turtle will be the winner
* Output the result. Let us know if we win or lose and the winner's color.

  
