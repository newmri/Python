import random

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT
    def can_create_car(self):
        return random.randint(1, 6) == 1

    def create_car(self):
        index = random.randint(0, len(COLORS) - 1)
        self.cars.append(Car(COLORS[index], (300, random.randint(-300, 300)), self.car_speed))

    def move(self):
        for car in self.cars:
            car.move()

    def is_hit(self, pos):
        for car in self.cars:
            if car.distance(pos) < 20:
                return True

        return False

    def level_up(self):
        self.car_speed += 1
