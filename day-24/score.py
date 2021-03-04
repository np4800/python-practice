from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.show_score()
    
    def show_score(self):
        self.goto(0,300)
        self.ht()
        self.clear()
        self.write(f"Score: {self.points}  High Score: {self.high_score}", True, "center", ("Arial",16,"normal"))
        
    def reset_game(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.show_score()
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", True, "center", ("Arial",16,"normal"))

    def update_score(self):
        self.points += 1
        self.show_score()