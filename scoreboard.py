from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-180, 270)
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="right", font=FONT)

    def rise_level(self):
        self.level += 1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
