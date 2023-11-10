from turtle import Turtle

class Car(Turtle):
    def __init__(self, color, pos, speed):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(color)
        self.goto(pos)
        self.speed = speed

    def move(self):
        self.forward(-self.speed)
