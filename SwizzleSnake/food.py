from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('pink')
        self.speed('fastest')
        self.refresh()

    #Refresh food to a random location.
    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 255)
        self.goto(random_x, random_y)