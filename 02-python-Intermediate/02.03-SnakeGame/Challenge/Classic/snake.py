import turtle as t

STARTING_POSITION = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # focus on the position of self head, it cannot place after self.segment
        self.head = self.segments[0]

    def create_snake(self):
        """Create an initial snake with three square"""
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        new_snake_seg = t.Turtle("square")
        new_snake_seg.color("white")
        new_snake_seg.penup()
        new_snake_seg.goto(position)
        self.segments.append(new_snake_seg)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """make the snake move"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """turn up snake's head"""
        # ba careful heading() is method
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """turn down snake's head """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """turn left snake's head"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """turn right snake's head"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
