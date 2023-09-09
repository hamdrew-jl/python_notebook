import turtle as t
import time
import snake
import food
import scoreboard

# Screen preparation
screen = t.Screen()
screen.setup(600, 600)
screen.title("Snake Game (Classic)")
screen.bgcolor("black")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

# key control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

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


screen.exitonclick()
