# Milan Palad
# ## ------------------------------------------------------- ## #
# ## ---------------------- Food Class --------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle
import random


# -------------------------- #
# Inherit from Turtle Class (Superclass)
class Food(Turtle):
    # TODO: Create food
    # -------------------------- #
    # Initializer
    # -------------------------- #
    def __init__(self):
        # Inherit from Turtle Class (Superclass)
        super().__init__()
        # Food Base
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # Generate food
        self.refresh()

    # -------------------------- #
    # Methods
    # -------------------------- #
    # TODO: Randomize position of food
    def refresh(self):
        """Sets food to a random position on the screen"""
        # Generate random coordinates for the food to go to
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # Set food to new position
        self.goto(random_x, random_y)
