# Milan Palad
# ## ------------------------------------------------------- ## #
# ## --------------------- Snake Class --------------------- ## #
# ## ------------------------------------------------------- ## #

# -------------------------- #
# Import Modules
# -------------------------- #
from turtle import Turtle

# -------------------------- #
# CONSTANTS
# -------------------------- #
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# -------------------------- #
# Class
# -------------------------- #
class Snake:
    # -------------------------- #
    # Initializer
    # -------------------------- #
    def __init__(self):
        # Empty segments
        self.segments = []
        # Create snake with segments
        self.create_snake()
        # Set head to first segment
        self.head = self.segments[0]

    # -------------------------- #
    # Methods
    # -------------------------- #
    # TODO: Create a snake body
    def create_snake(self):
        """Creates a basic snake body with three segments"""

        # Base Coordinate
        x = 0
        y = 0
        # Create three body segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # TODO: Extend snake body
    def add_segment(self, position):
        """Adds segment to snake"""
        # Create object
        new_segment = Turtle("square")
        # Set color
        new_segment.color("white")
        # Pull pen up for no line
        new_segment.penup()
        # Place in position
        new_segment.goto(position)
        # Add segment to list
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the end of the snake"""
        self.add_segment(self.segments[-1].position())

    # TODO: Move the snake
    def move(self):
        """Moves the snake segments forward"""
        # Move segments (back to front - (start, stop, step)) to follow the first (head)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get coordinates of segment in front of the current segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Set coordinates to new coordinates to move it to new position
            self.segments[seg_num].goto(new_x, new_y)
        # Move head forward
        self.head.forward(MOVE_DISTANCE)

    # TODO: Move snakes with keystrokes
    def up(self):
        """Turns snake to go up"""
        # Check if head is currently not moving down before moving up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns snake to go down"""
        # Check if head is currently not moving up before moving down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns snake to go left"""
        # Check if head is currently not moving right before moving left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns snake to go right"""
        # Check if head is currently not moving left before moving right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
