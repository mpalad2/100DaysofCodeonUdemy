# Milan Palad
# ## ------------------------------------------------------- ## #
# ## ------------------ Turtle Crossing -------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# -------------------------- #
# CONSTANTS
# -------------------------- #


# -------------------------- #
# Base Code
# -------------------------- #

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# Create turtle player
player = Player()

# Create scoreboard
scoreboard = Scoreboard()

# Turn on listener
screen.listen()
# Player Key Movement
screen.onkey(fun=player.go_up, key="w")

# Default game running value
game_is_on = True

# Create a car manager
car_manager = CarManager()

# While game is running
while game_is_on:
    # Update according to level speed
    time.sleep(player.level_speed)
    screen.update()
    # move car towards the edge
    car_manager.move()

    # Add car
    car_manager.add_car()

    # Check if turtle finishes level
    if player.ycor() > 280:
        # Reset position
        player.reset_position()
        # Increase score
        scoreboard.increase_score()

    # Check if turtle hits a car
    for car in car_manager.cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False


# Exit on click
screen.exitonclick()
