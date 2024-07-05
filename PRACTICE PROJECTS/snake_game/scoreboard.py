from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.color("white")
        self.write_score()

    def increase_points(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score:  {self.score}  | High Score: {self.high_score}", move=False, align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                 file.write(str(self.score))
        self.high_score = self.score
        self.score = 0
        self.write_score()



