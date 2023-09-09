# SnakeGame(Classic)

Split into seven steps
* 01 create a snake body
* 02 move the snake
* 03 control the snake
* 04 detect collision with food
* 05 create a scoreboard
* 06 detect collision with wall
* 07 detect collision with tail

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
### 1.2 Create initial snake
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
    # need to be check the order weather it need to reverse or not(-1 or 1)
    # the number represent in range(start= , end=, steps= )
    for seg_num in range(0, len(full_body) - 1, 1):
        new_x = full_body[seg_num + 1].xcor()
        new_y = full_body[seg_num + 1].ycor()
        full_body[seg_num].goto(new_x, new_y)

    full_body[len(full_body) - 1].forward(20)
    full_body[len(full_body) - 1].left(90)

```

