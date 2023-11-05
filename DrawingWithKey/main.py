from turtle import Turtle, Screen

class Movement:
    def __init__(self, speed):
        self.speed = speed
        self.degree = 0

    def forward(self):
        turtle.forward(self.speed)

    def backward(self):
        turtle.back(self.speed)

    def right(self):
        self.degree = (self.degree - self.speed) % -360
        turtle.setheading(self.degree)

    def left(self):
        self.degree = (self.degree + self.speed) % 360
        turtle.setheading(self.degree)

    def clear(self):
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()

turtle = Turtle()
screen = Screen()
movement = Movement(10)

screen.listen()

screen.onkey(key="w", fun=movement.forward)
screen.onkey(key="s", fun=movement.backward)
screen.onkey(key="d", fun=movement.right)
screen.onkey(key="a", fun=movement.left)
screen.onkey(key="c", fun=movement.clear)

screen.exitonclick()