from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_distance = STARTING_MOVE_DISTANCE
        self.move_inc = MOVE_INCREMENT
        self.shape("square")
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.x = 320
        self.y = random.randint(-240, 280)
        self.goto(self.x, self.y)

    def move(self):
        self.x -= self.starting_distance
        self.goto(self.x, self.y)

    def stage_clear(self, level):
        self.home()
        self.starting_distance += (self.move_inc * level)
