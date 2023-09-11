# SnakeGame(Classic)


Split into seven steps
* 01 create a snake body
* 02 move the snake
* 03 control the snake
* 04 detect collision with food
* 05 create a scoreboard
* 06 detect collision with wall
* 07 detect collision with tail

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/59583fb5-ed76-4863-a579-14555b1be80c)

* Record the High score when playing the game -> go to challenge ->add high score file

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/ff377d90-9f85-4464-a6df-b36762ffcdd6)


## 01 create a snake body

### 1.1 set the screen
```python
import turtle as t
import time
import snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)
```
### 1.2 Create an initial snake
```python

start_position = [(-40, 0), (-20, 0), (0, 0)]
for i in start_position:
    new_snake_seg = t.Turtle("square")
    new_snake_seg.color("white")
    new_snake_seg.penup()
    new_snake_seg.goto(i)
    full_body.append(new_snake_seg)
```

### 1.3 Make a movement
```python
full_body = []

is_go_on = True
while is_go_on:
    screen.update()
    time.sleep(0.1)

    # [IMPORTANT] the content inside range(),
    # need to check the order whether it needs to reverse or not(-1 or 1)
    # the number represent in range(start= , end=, steps= )
    for seg_num in range(0, len(full_body) - 1, 1):
        new_x = full_body[seg_num + 1].xcor()
        new_y = full_body[seg_num + 1].ycor()
        full_body[seg_num].goto(new_x, new_y)

    full_body[len(full_body) - 1].forward(20)
    full_body[len(full_body) - 1].left(90)

```

### 1.4 Manage three class Snake, Food, Scoreboard in separate files
* Create class Snake in a file named snake.py, and change some code in the main program
* Need to change some code above.
#### 1.4.1 class snake
```python
import turtle as t

STARTING_POSITION = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # focus on the position of self head, it cannot place after self.segment
        self.head = self.segments[0]

    def create_snake(self):
        """Create an initial snake with three square"""
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        new_snake_seg = t.Turtle("square")
        new_snake_seg.color("white")
        new_snake_seg.penup()
        new_snake_seg.goto(position)
        self.segments.append(new_snake_seg)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """make the snake move"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """turn up snake's head"""
        # ba careful heading() is method
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """turn down snake's head """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """turn left snake's head"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """turn right snake's head"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
```
#### 1.4.2 class food
```python
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.speed(0)
        self.color("lightblue")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
```
#### 1.4.3 class scoreboard
```python
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 10, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("arial", 40, "bold"))
```

### 1.5 Call class Snake, Food, Scoreboard in main.py

```python
import snake
import food
import scoreboard

snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()
```

* Replace some code by calling method
* Detect collision with food
* Detect collision with wall
* Detect collision with tail

```python
is_go_on = True
while is_go_on:
    screen.update()  # refresh the screen
    time.sleep(0.1)  # delay the refresh

    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        score.add_score()
        snake.extend()
        food.refresh()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_go_on = False
        score.game_over()

    # detect collision with tail
    # if head collision with any segment in the tail -> game over
    for segment in snake.segments[1:]:
        if len(snake.segments) > 3 and snake.head.distance(segment) < 10:
            is_go_on = False
            score.game_over()
```
