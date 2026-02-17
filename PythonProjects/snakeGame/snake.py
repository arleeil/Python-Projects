from turtle import Turtle
SET_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head= self.segments[0]

    def create_snake(self):
        for x in SET_POSITIONS:
            self.add_segment(x)

    def add_segment(self, position):
            new_seg = Turtle('square')
            new_seg.color('white')
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)
    def reset(self):
        for x in self.segments:
            x.goto(x= 1000, y=1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
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

