import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# screen setting
screen = Screen()
screen.bgcolor("black")
screen.title("Pingpong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# pingpong area dot line
writer = Turtle("square")
writer.shapesize(stretch_wid=0.1, stretch_len=0.6)
writer.color("white")
writer.hideturtle()
writer.speed(0)
writer.penup()
for y in range(-300, 300, 20):
    writer.goto(0, y)
    writer.setheading(90)
    writer.stamp()
    writer.forward(10)

# Call the class
paddle_left = Paddle((-380, 0))
paddle_right = Paddle((380, 0))
ball = Ball()
score = Scoreboard()

# Listen
screen.listen()
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")

is_go_on = True
while is_go_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ((ball.distance(paddle_right) < 50 and ball.xcor() > 360)
            or (ball.distance(paddle_left) < 50 and ball.xcor() < -360)):
        ball.bounce_x()

    # Detect R paddle missing
    if ball.xcor() > 400:
        score.add_score_l()
        ball.reset_position()

    # Detect l paddle missing
    if ball.xcor() < -400:
        score.add_score_r()
        ball.reset_position()

screen.exitonclick()
