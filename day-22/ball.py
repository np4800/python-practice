from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(2,2)
        self.penup()
        self.xpos = 10
        self.ypos = 10
        self.move_speed = 0.1

    
    def move(self):
        new_x = self.xcor() + self.xpos
        new_y = self.ycor() + self.ypos
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ypos *= -1

    def bounce_x(self):
        self.xpos *= -1
        self.move_speed *= 0.9
