# Milan Palad
# ## ------------------------------------------------------- ## #
# ## --------------------- Snake Game ---------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# -------------------------- #
# Base Code
# -------------------------- #
# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turn off tracer for animation
screen.tracer(0)

# Create snake
snake = Snake()
# Create food
food = Food()
# Create scoreboard
scoreboard = Scoreboard()

# Turn on listen for user keystrokes
screen.listen()
# User Keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Base Game Playing Value
game_is_on = True

# While game is active
while game_is_on:
    # Update screen
    screen.update()
    # Add sleep for smoother animation
    time.sleep(0.1)
    # Move snake
    snake.move()

    # Check for snake and food collision
    if snake.head.distance(food) < 15:
        # Update food position
        food.refresh()
        # Extend snake
        snake.extend()
        # Update scoreboard
        scoreboard.increase_score()

    # Check for snake collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # Game over
        game_is_on = False
        scoreboard.game_over()

    # Check for snake head collision with tail (skip head - start at 1)
    for segment in snake.segments[1:]:
        # If head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            # Game over
            game_is_on = False
            scoreboard.game_over()


# Exit on click
screen.exitonclick()