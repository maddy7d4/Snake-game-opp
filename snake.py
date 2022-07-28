# This are the cordinates where the squares should placed.
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

import turtle


class Snake:

    def __init__(self):
        self.new_turtle = []
        self.create_turtle()
        self.head = self.new_turtle[0]

    def create_turtle(self):
        # creating three objects for Turtle class in for loop.
        for position in STARTING_POSITION:
            self.addSegment(position)

    def addSegment(self,position):
        t = turtle.Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        # appending each object to empty list called new_turtle[].
        self.new_turtle.append(t)

    def extend(self):
        self.addSegment(position=self.new_turtle[-1].position())

    def move(self):
        # making the last square to previous square position.
        for j in range(len(self.new_turtle) - 1, 0, -1):
            new_x = self.new_turtle[j - 1].xcor()
            new_y = self.new_turtle[j - 1].ycor()
            self.new_turtle[j].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

