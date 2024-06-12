from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.pu()
        self.goto(position)

    def move_paddle_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.sety(0)