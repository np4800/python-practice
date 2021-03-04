from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.goto(-200,280)
        self.write(f"Level: {self.level}",align="center",font=("Courier",16,"normal"))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Courier",16,"normal"))