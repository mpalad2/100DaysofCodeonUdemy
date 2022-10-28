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
ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")
GAME_OVER_FONT = ("Courier", 20, "bold")


# -------------------------- #
# Class
# -------------------------- #
# Inherit from Turtle Class (Superclass)
class Scoreboard(Turtle):
    # TODO: Create a scoreboard
    # -------------------------- #
    # Initializer
    # -------------------------- #
    def __init__(self):
        # Inherit from Turtle Class (Superclass)
        super().__init__()
        # Hide turtle
        self.hideturtle()
        # Base Score
        self.penup()
        self.color("white")
        self.score = 0
        # Set position
        self.goto(0, 280)
        # Write base scoreboard on screen
        self.update_scoreboard()

    # -------------------------- #
    # Methods
    # -------------------------- #
    # TODO: Update and increase score on scoreboard
    def update_scoreboard(self):
        """Updates scoreboard visual"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases score by one and updates scoreboard"""
        # Add one to score
        self.score += 1
        # Clear screen
        self.clear()
        # Update scoreboard on screen
        self.update_scoreboard()

    def game_over(self):
        """Prints out game over to the user"""
        # Move position to center
        self.goto(0, 0)
        # Print out game over
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
