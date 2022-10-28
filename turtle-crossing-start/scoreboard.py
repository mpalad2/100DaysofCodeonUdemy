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
FONT = ("Courier", 14, "normal")


# -------------------------- #
# Class
# -------------------------- #


class Scoreboard(Turtle):
    def __init__(self):
        # Import Turtle superclass
        super().__init__()
        # Scoreboard base
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250, 270)
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the score on the scoreboard"""
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        """Increase the score by one"""
        # Clears previous score
        self.clear()
        # Add one to score
        self.score += 1
        # Update new score
        self.update_scoreboard()

    def game_over(self):
        """Prints out game over when player is hit"""
        # Move to center
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
