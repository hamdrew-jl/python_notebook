from turtle import Turtle
import random


# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPE = ["car1.gif", "car2.gif", "car3.gif", "car4.gif", "car5.gif"]
Y_COORDS = [-224, -194, -164, -134, -104, -74, -44, -14, 16, 46, 76, 106, 136, 166, 196, 230]
X_COORDS = [320, 350, 390, 420, 450]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            shape = random.choice(SHAPE)
            new_cars = Turtle()
            new_cars.shape(shape)
            new_cars.penup()
            new_cars.goto(random.choice(X_COORDS), random.choice(Y_COORDS))
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
