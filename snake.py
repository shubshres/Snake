from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds a new segment to the snake"""
        body_segment = Turtle("square")
        body_segment.color("white")
        body_segment.penup()
        body_segment.goto(position)
        self.body.append(body_segment)

    def grow(self):
        """adds a new segment to the snake after eating food"""
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            x_cor = self.body[seg_num - 1].xcor()
            y_cor = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(x_cor, y_cor)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

