# Milan Palad
# ## ------------------------------------------------------- ## #
# ## --------------------- Paddle Class -------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle

# -------------------------- #
# CONSTANTS
# -------------------------- #
STR_WIDTH = 5
STR_LEN = 1


# -------------------------- #
# Class
# -------------------------- #
class Paddle(Turtle):
    # -------------------------- #
    # Initializer
    # -------------------------- #
    def __init__(self, position):
        """Creates a paddle object"""
        # Import Turtle Superclass
        super().__init__()
        # Paddle Base
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=STR_WIDTH, stretch_len=STR_LEN)
        self.goto(position)

    # -------------------------- #
    # Methods
    # -------------------------- #
    def go_up(self):
        """Moves the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
