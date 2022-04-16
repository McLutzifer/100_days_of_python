from secrets import choice
from turtle import Turtle, Screen
import random

colors = [
    "pale green",
    "dark turquoise",
    "light slate gray",
    "plum",
    "blanched almond",
    "sky blue",
    "light gray",
    "light salmon"
]

directions = [0, 90, 180, 270]

turtle = Turtle()
turtle.pensize(10)
turtle.shape("turtle")
turtle.speed(6)

for _ in range(200):
    turtle.forward(30)
    turtle.right(random.choice(directions))
    turtle.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
