import turtle as t
import random

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim = t.Turtle()
t.colormode(255)

tim.shape("circle")
tim.pensize(10)
tim.speed(10)
directions = [0, 90, 180, 270]
screen = t.Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

for _ in range(0,200):
    tim.pencolor(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(20)
    
    # screen.exitonclick()