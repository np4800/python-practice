from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

game_is_on = True

screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((420,0))
l_paddle = Paddle((-430,0))

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

ball = Ball()
score = Score()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision of the 4 walls
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y() 

    # Detect Collision on the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 400 or ball.distance(l_paddle) < 50 and ball.xcor() < -400:
        ball.bounce_x()
        
    elif ball.xcor() > 480:
        # print(ball.xcor())
        ball.home()
        ball.bounce_x()
        score.l_point()
        ball.move_speed = 0.1
    elif ball.xcor() < -480:
        ball.home()
        ball.bounce_x()
        score.r_point()
        ball.move_speed = 0.1

screen.exitonclick()