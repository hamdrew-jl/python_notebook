from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


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
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()