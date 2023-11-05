import random
from turtle import Turtle, Screen

TUTLE_SIZE = 20
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
GOAL = SCREEN_WIDTH / 2 - TUTLE_SIZE

class MyTurtle:
    def __init__(self, color, y):
        self.turtle = Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x=-230, y= y)

    def move(self):
        self.turtle.forward(random.randint(0, 10))
        if self.turtle.xcor() >= GOAL:
            screen.title(f"Winner is {self.turtle.color()[0]}")
            return True
        return False

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtleList = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = SCREEN_HEIGHT / 2 - TUTLE_SIZE
for i in range(0, 6):
    turtle = MyTurtle(colors[i], y)
    y -= SCREEN_HEIGHT / 6
    turtleList.append(turtle)

running = True
while running:
    for t in turtleList:
        if t.move():
            running = False

screen.exitonclick()