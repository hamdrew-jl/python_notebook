# Pingpong Game

## 01 Screen Setting and Background image drawing
```python
# screen setting
screen = Screen()
screen.bgcolor("black")
screen.title("Pingpong Game")
screen.setup(width=800, height=600)
screen.tracer(0)
```        

```python
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
```
## 02 Set class Paddle
* make the paddle move up and down
* limit the paddle with in the screen
* use global variables for future adjustment

```python
from turtle import Turtle


LIMIT_NUM = 265
MOVE_SPEED = 40
PADDLE_LENGTH = 5


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(PADDLE_LENGTH, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < LIMIT_NUM - MOVE_SPEED: # limit the paddle with in the screen
            new_y = self.ycor() + MOVE_SPEED
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -(LIMIT_NUM - MOVE_SPEED): # limit the paddle with in the screen
            new_y = self.ycor() - MOVE_SPEED
            self.goto(self.xcor(), new_y)
```
## 03 Set class Ball
* ball place in the center when the game start
* ball move 
* when the ball hit the boundary, it changes the move direction
* when ball hit the left and right wall, it'll reset podition in the center  

```python
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        # added one extra move in ball.bounce_x, so that it moves ball away from the paddle
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.move_speed *= 0.9

    def reset_position(self):
            self.goto(0, 0)
            self.move_speed = 0.1
            self.bounce_x()

```
## 04 Set class Scoreboard
* This is a two-player game. Calculate the score separately.
* Show initial score on the screen
* add score 

```python
from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-50, 200)
        self.write(f"{self.score_l}", align=ALIGNMENT, font=FONT)
        self.goto(50, 200)
        self.write(f"{self.score_r}", align=ALIGNMENT, font=FONT)

    def add_score_l(self):
        self.clear()
        self.score_l += 1
        self.update_score()

    def add_score_r(self):
        self.clear()
        self.score_r += 1
        self.update_score()

```
## 05 Main program
```python
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
```