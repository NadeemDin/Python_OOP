from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/Pyrex_000/Desktop/data.txt","r") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("White")
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.highscore} ", False, "center", ("Courier", 12, "normal"))



    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/Users/Pyrex_000/Desktop/data.txt","w") as data:
                data.write(f"{self.score}")

        self.score = 0
        self.update_score()






