# Milan Palad
# ## ------------------------------------------------------- ## #
# ## ------------------ Scoreboard Class ------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle

# -------------------------- #
# CONSTANTS
# -------------------------- #
FONT = ("Courier", 50, "normal")

# -------------------------- #
# Class
# -------------------------- #
class Scoreboard(Turtle):
    def __init__(self):
        """Creates a scoreboard object"""
        # Import Turtle Superclass
        super().__init__()
        # Scoreboard Base
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.goto(-150, 240)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(150, 240)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        """Adds point to left paddle/player on scoreboard"""
        # Clear screen
        self.clear()
        # Add point
        self.l_score += 1
        # Update scoreboard
        self.update_scoreboard()

    def r_point(self):
        """Adds point to right paddle/player on scoreboard"""
        # Clear screen
        self.clear()
        # Add point
        self.r_score += 1
        # Update scoreboard
        self.update_scoreboard()
