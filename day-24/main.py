from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.title("Snake Game")
screen.listen()
snake = Snake()
score = Score()
snake_food = Food()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True

while game_is_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()

    # Detect collision here using distance method of screen
    if snake.segments[0].distance(snake_food) < 15:
        snake_food.refresh()
        snake.extend_segement()
        score.update_score()

    # Detect collision with wall for game over
    if snake.segments[0].xcor() > 420 or snake.segments[0].xcor() < -420 or snake.segments[0].ycor() > 420 or snake.segments[0].ycor() < -420:
        # game_is_on = False
        # score.game_over()
        score.reset_game()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset_game()
            snake.reset()

screen.exitonclick()