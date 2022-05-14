from turtle import Turtle
from random import randint, choice

SHAPES = ['circle', 'square']
COLOURS = ['deeppink', 'springgreen', 'orange', 'coral']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food_generator()

    def food_generator(self):
        """
        Creates food object at random coordinate.
        """
        self.shape(choice(SHAPES))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(choice(COLOURS))
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """
        Creates new food placement coordinates.
        """
        random_x, random_y = randint(-270, 270), randint(-270, 270)
        self.goto(random_x, random_y)
        self.color(choice(COLOURS))
        self.shape(choice(SHAPES))





