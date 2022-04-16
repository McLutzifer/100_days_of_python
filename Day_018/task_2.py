from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

colors  = ["red","green","blue","orange","purple","pink","yellow"]

for i in range (3, 11):
    for j in range (i):
        turtle.forward(100)
        turtle.right(360/i)
    turtle.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
