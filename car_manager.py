from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_quantity = 10
    
    
    def create_cars(self):
        random_y = random.randint(-250, 250)
        if random_y % self.car_quantity == 0:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def move_forward(self):
        for self.car in self.all_cars:
            self.car.backward(self.car_speed)

    def remove_car(self):
        for self.car in self.all_cars:
            if self.car.xcor() < -280:
                self.all_cars.remove(self.car)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.car_quantity > 2:
            self.car_quantity -= 2