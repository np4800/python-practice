from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + 5
        x_pos = self.xcor()
        self.goto(x_pos,new_y)

    def go_to_start(self):
        self.goto(0,-280)