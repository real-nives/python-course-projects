from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #Adds a segment at the tail of the snake.
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    #Extends the snake.
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    #Shifts all snake segments forward.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #Points the snake up.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    #Points the snake left.
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    #Points the snake down.
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    #Points the snake right.
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)