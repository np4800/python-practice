from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-150,300)
        self.write(f"{self.l_score}",align="center",font=("Courier",80,"normal"))
        self.goto(150,300)
        self.write(f"{self.r_score}",align="center",font=("Courier",80,"normal"))

    def r_point(self):
        self.r_score += 1
        self.updatescore()

    def l_point(self):
        self.l_score += 1
        self.updatescore()