from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

colors  = ["red","green","blue","orange","purple","pink","yellow"]

# def change_color():
#     R = random.randrange(0, 257, 10)
#     G = random.randrange(0, 257, 10)
#     B = random.randrange(0, 257, 10)

#     return R, G, B


for i in range (4, 19):
    for j in range (i):
        turtle.forward(100)
        turtle.right(360/i)
    color = random.choice(colors)
    #r, g, b = change_color()
    #turtle.color(r, g, b)
    turtle.color(color)



screen = Screen()
screen.exitonclick()
