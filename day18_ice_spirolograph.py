import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(10)
screen = t.Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)


# tim.reset()
# tim.shape("circle")
# tim.shapesize(5,2)
# tim.settiltangle(45)
# tim.fd(50)
# tim.settiltangle(-45)
# tim.fd(50)

# screen.exitonclick()

for _ in range(0,100):
    tim.color(random_color())
    tim.circle(100)
    tim.tiltangle(30)
    # tim.fd(50)
    tim.lt(50)