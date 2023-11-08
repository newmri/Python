from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PongGame")
screen.tracer(0)

scroe_board = Scoreboard()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

isRunning = True
while isRunning:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        scroe_board.add_l_score()

    if ball.xcor() < -380:
        ball.reset_pos()
        scroe_board.add_r_score()

screen.exitonclick()