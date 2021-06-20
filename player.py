from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def moving_up(self):
        self.forward(MOVE_DISTANCE)

    def moving_down(self):
        self.backward(MOVE_DISTANCE)

    def stage_clear(self):
        self.goto(STARTING_POSITION)

