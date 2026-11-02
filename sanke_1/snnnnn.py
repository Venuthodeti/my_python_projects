from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD =20
RIGHT=0
LEFT=180
UP=90
DOWN=270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for pos in POSITIONS:
           self.add_segment(pos)

    def move (self):
        for segment in range (len(self.segments)-1, 0 ,-1):
            new_x=self.segments[segment-1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)
    def add_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def y_axis(self):
        self.head = self.segments[0]
        self.head.goto(self.segments[0].xcor(), -self.segments[0].ycor())
    def x_axis(self):
        self.head = self.segments[0]
        self.head.goto(-self.segments[0].xcor(), self.segments[0].ycor())

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