from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.ht()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(n):
    angle = 360/n
    for _ in range(n):
        tim.forward(100)
        tim.right(angle)

for shape_size in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_size)

tim.circle()
screen = Screen()
screen.exitonclick()

# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown() 
