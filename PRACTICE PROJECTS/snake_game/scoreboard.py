from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.color("white")
        self.write_score()

    def increase_points(self):
        self.points += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score:  {self.points}", move=False, align='center', font=('Arial', 14, 'normal'))
