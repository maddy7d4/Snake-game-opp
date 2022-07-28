from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.score()
    def score(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=250)
        self.write(f'Score : {self.points}',move = False,align = 'center',font=('courier',20,'normal'))

    def increase_score(self):
        self.points += 1
        self.clear()
        self.score()