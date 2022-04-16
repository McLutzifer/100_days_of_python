import turtle
import random

my_turtle = turtle.Turtle()
turtle.colormode(255)
my_turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

number_of_circles = 100

for _ in range(number_of_circles):
    my_turtle.color(random_color())
    my_turtle.circle(200)
    my_turtle.right(360/number_of_circles)
    

screen = turtle.Screen()
screen.exitonclick()