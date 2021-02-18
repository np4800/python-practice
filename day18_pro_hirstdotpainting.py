import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpeg',30)
range_colors=[]
t.colormode(255)
tim = t.Turtle()
tim.shape("circle")
screen = t.Screen()

for item in colors:
    rgb = (item.rgb.r,item.rgb.g,item.rgb.b)
    range_colors.append(rgb)

tim.speed("fastest")
tim.penup()
tim.setpos(-250,-250)
tim.pendown()

for y in range(-250,250,50):
    for x in range(-250,250,50):
        tim.setpos(x,y)
        tim.pendown()
        tim.dot(20,random.choice(range_colors))
        tim.penup()


screen.exitonclick()