from turtle import Turtle


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.color("white")
        self.shape("square")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)