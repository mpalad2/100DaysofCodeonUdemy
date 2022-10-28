# Milan Palad
# ## ------------------------------------------------------- ## #
# ## ------------------ Car Manager Class ------------------ ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle
import random

# -------------------------- #
# CONSTANTS
# -------------------------- #
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STR_WIDTH = 1
STR_LEN = 2


# -------------------------- #
# Class
# -------------------------- #
class CarManager(Turtle):
    def __init__(self):
        """Creates car manager with set of cars"""
        # Empty car list
        self.cars = []
        # Add cars
        self.add_car()

    def add_car(self):
        """Creates a car object"""
        # Random 1 in 6th chance a car is made (minimizes frequency)
        chance = random.randint(1, 6)
        # Only if chance is 1 will a car be made
        if chance == 1:
            # Create object
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=STR_WIDTH, stretch_len=STR_LEN)
            # Generate random color for car
            car_color = random.choice(COLORS)
            new_car.color(car_color)
            # Go to random coordinate along the y-axis
            y_pos = random.randint(-250, 250)
            x_pos = random.randint(300, 400)
            new_car.goto(x_pos, y_pos)
            # Add to car list
            self.cars.append(new_car)

    def move(self):
        """Moves car across the screen"""
        for car in self.cars:
            car.forward(10)
