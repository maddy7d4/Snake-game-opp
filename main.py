from turtle import Turtle,Screen
import random
import time
from snake import Snake
import food
from scoreboard import Scoreboard

t = Turtle()
t.penup()
screen = Screen()
screen.setup()
screen.bgcolor("black")
screen.title("My Snake Game")
food = food.Food()

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.tracer(0)
is_on = True
score = Scoreboard()
score.score()


while is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()>340 or snake.head.xcor()<-340 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        # t.color("white")
        # t.write("Game  Over",align='center',font=('courier',28,'normal'))

        snake.reset()
    for i in snake.new_turtle[1:]:
        if snake.head.distance(i) < 10:
            score.reset()
            # is_on = False
            # t.color("white")
            # t.write("Game  Over", align='center', font=('courier', 28, 'normal'))


screen.exitonclick()
