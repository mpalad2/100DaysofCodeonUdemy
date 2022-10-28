# Milan Palad
# ## ------------------------------------------------------- ## #
# ## ---------------------- Ball Class --------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle

# -------------------------- #
# CONSTANTS
# -------------------------- #


# -------------------------- #
# Class
# -------------------------- #
class Ball(Turtle):
    def __init__(self):
        """Creates a ball object"""
        # Import Turtle Superclass
        super().__init__()
        # Ball Base
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounces the ball when it hits a wall (switch y direction)"""
        # Multiply y move by -1 to switch directions
        self.y_move *= -1

    def bounce_x(self):
        """Bounces the ball when it hits a paddle (switch x direction)"""
        # Multiply y move by -1 to switch directions
        self.x_move *= -1
        # Change move speed to make the ball go faster
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets ball to middle of screen and serves to other paddle after paddle misses"""
        # Reset ball position to middle of screen
        self.goto(0, 0)
        # Reset speed of ball to default
        self.move_speed = 0.1
        # Invert x movement to start moving towards other player
        self.bounce_x()


