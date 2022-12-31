from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-280,-280)
        self.write(self.score, align="left", font=("courier", 50, "normal"))


    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("courier", 50, "normal"))

