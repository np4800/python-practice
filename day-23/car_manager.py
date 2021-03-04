from turtle import Turtle
import random

CAR_COLOR = ['blue', 'yellow', 'red', 'green', 'black', 'purple', 'orange']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Carmanager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance % 6 == 0:     
            rand_color = random.choice(CAR_COLOR)
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.color(rand_color)
            new_car.penup()
            y_pos = random.randint(-250,250)
            new_car.goto((300,y_pos))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

