# Milan Palad
# ## ------------------------------------------------------- ## #
# ## -------------------- Player Class --------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle

# -------------------------- #
# CONSTANTS
# -------------------------- #
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# -------------------------- #
# Class
# -------------------------- #
class Player(Turtle):
    def __init__(self):
        """Creates a player object"""
        # Import Turtle superclass
        super().__init__()
        # Turtle Player Base
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)
        # Level Speed
        self.level_speed = 0.1

    def go_up(self):
        """Moves the turtle forward"""
        self.forward(MOVE_DISTANCE) # CHANGE TO MOVE_DISTANCE LATER

    def reset_position(self):
        """Resets player to starting position whenever they finish a level"""
        self.goto(0, -280)
        # Increase level speed
        self.level_speed *= 0.7
