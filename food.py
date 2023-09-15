from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("#176B87")
        self.speed("fastest")
        self.relocate()
    def relocate(self):
        rand_x = randint(-270, 270)
        rand_y = randint(-270, 270)
        self.goto(rand_x, rand_y)

