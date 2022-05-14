from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP, DOWN = 90, 270
LEFT, RIGHT = 180, 0



class Snake:

    def __init__(self):
        self.move_distance = 20
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates snake body with three separate segments.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds segment to snake's body.
        """
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """
        Adds segment to end of snake's body.
        """
        position = self.segments[-1].position()
        self.add_segment(position)

    def move(self):
        """
        Moves snake.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(self.move_distance)

    # directional arrow inputs:
    def up(self):
        """
        Moves head of snake up.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Moves head of snake down.
        """
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        """
        Moves head of snake left.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Moves head of snake right.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


