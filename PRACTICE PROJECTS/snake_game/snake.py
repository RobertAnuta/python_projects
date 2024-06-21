from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10


class Snake:
    def __init__(self):
        self.body_length = []
        self.create_snake()
        self.head = self.body_length[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        turtle_body = Turtle(shape="square")
        turtle_body.color("white")
        turtle_body.penup()
        turtle_body.goto(position)
        self.body_length.append(turtle_body)

    def extend(self):
        self.add_segment(self.body_length[-1].position())

    def move(self):
        for segment in range(len(self.body_length) - 1, 0, -1):
            new_x = self.body_length[segment - 1].xcor()
            new_y = self.body_length[segment - 1].ycor()
            self.body_length[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
