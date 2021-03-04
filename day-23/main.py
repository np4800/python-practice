import time
from player import Player
from scoreboard import Scoreboard
from car_manager import Carmanager
from turtle import Screen

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()

game_is_on = True
car_manager = Carmanager()
player = Player()
score = Scoreboard()
screen.onkey(player.up,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect Collision with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 290:
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()

