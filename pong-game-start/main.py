# Milan Palad
# ## ------------------------------------------------------- ## #
# ## ---------------------- Pong Game ---------------------- ## #
# ## ------------------------------------------------------- ## #
import time
# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# -------------------------- #
# Base Code
# -------------------------- #
# TODO: Create the screen

# Create screen
screen = Screen()
screen.screensize(canvheight=600, canvwidth=800)
screen.bgcolor("black")
screen.title("Pong")
# Set tracer to 0 until the game is set up
screen.tracer(0)

# Set screen listener
screen.listen()

# TODO: Create and move a paddle

# Create player (right) paddle
right_paddle = Paddle((350, 0))

# Move paddle
screen.onkeypress(fun=right_paddle.go_up, key="Up")
screen.onkeypress(fun=right_paddle.go_down, key="Down")

# TODO: Create another paddle
# Create another (left) paddle
left_paddle = Paddle((-350, 0))

# Move paddle
screen.onkeypress(fun=left_paddle.go_up, key="w")
screen.onkeypress(fun=left_paddle.go_down, key="s")

# TODO: Create the ball and make it move
# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Default Game Running Value
game_is_on = True

# While game is running
while game_is_on:
    # Sleep set to ball movement
    time.sleep(ball.move_speed)
    # Update screen
    screen.update()
    # Move ball
    ball.move()

    # TODO: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO: Detect collision with paddle

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO: Detect when paddle misses and keep score
    # Right paddle/player misses
    if ball.xcor() > 350:
        # Reset position
        ball.reset_position()
        # Add point to opposite paddle/player
        scoreboard.l_point()

    # Left paddle/player misses
    if ball.xcor() < -350:
        ball.reset_position()
        # Add point to opposite paddle/player
        scoreboard.r_point()

# Exit on click
screen.exitonclick()