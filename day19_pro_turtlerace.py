import turtle as t
import random

colors = ["red","blue","green","yellow","purple","orange"]
all_turtle = []
screen = t.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter color: ")

is_race_on = False
y=100
i=0

for tim in colors:
    tim = t.Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(colors[i])
    tim.goto(x=-230,y=y)
    y -= 50
    i += 1
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on =  False
            if turtle.pencolor() == user_bet:
                print(f"You won the bet: {turtle.pencolor()} is first in the race!")
            else:
                print(f"You lost the bet: {turtle.pencolor()} is first in the race!")

        else:
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance) 

screen.exitonclick()