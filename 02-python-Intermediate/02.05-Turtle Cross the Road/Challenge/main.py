import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_manager = CarManager()
score = Scoreboard()
score.level_up()

# listen
screen.listen()
screen.onkey(tim.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.random_cars()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            score.game_over()

    if tim.is_at_finish_line():
        tim.reset_position()
        car_manager.move_increment()
        score.level_up()


screen.exitonclick()










