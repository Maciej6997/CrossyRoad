from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.setposition(STARTING_POSITION)
        self.move = MOVE_DISTANCE
        self.speed(10)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + self.move)

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.move += 5
