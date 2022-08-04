from asyncore import write
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score()
    def score(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.points} High Score : {self.highscore}',move = False,align = 'center',font=('courier',20,'normal'))


    def reset(self):
        if self.points>self.highscore:
            self.highscore = self.points
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.points = 0
        self.update_scoreboard()

    def increase_score(self):
        self.points += 1
        self.clear()
        self.score()
