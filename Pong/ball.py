from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.rand_angle()

    def move_forward(self):
        self.forward(5)

    def rand_angle(self):
        new_angle = randint(0, 360)
        if new_angle > 60 and new_angle < 120:
            if new_angle > 90:
                new_angle += 45
            else:
                new_angle -= 45
        elif new_angle > 240 and new_angle < 300:
            if new_angle > 270:
                new_angle += 45
            else:
                new_angle -= 45
        self.setheading(new_angle)

    def bounce_y(self):
        self.setheading(360 - self.heading())

    def bounce_x(self):
        self.setheading((180 - self.heading()) + randint(-10, 10))
        
    def reset_position(self):
        self.setpos(0,0)
        self.rand_angle()