import random
from extraction import rgb_colors
import turtle

# rgb_colors = [(235, 230, 233), (224, 233, 229), (40, 98, 148), (178, 46, 78), (205, 160, 93), (224, 210, 102),
#               (137, 89, 63), (178, 165, 36), (110, 175, 208), (213, 130, 174), (228, 72, 48), (201, 74, 117),
#               (92, 103, 188), (22, 154, 87), (122, 217, 208), (126, 41, 70), (95, 158, 62), (45, 190, 204),
#               (226, 171, 187), (130, 189, 161), (213, 206, 38), (232, 171, 163), (172, 186, 222), (153, 208, 218),
#               (104, 50, 38), (45, 62, 101), (44, 75, 80), (51, 61, 71)]
color_list = rgb_colors[2:]
# getting rid of the first colors because
# they are shades of white/light grey fom the background


my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
turtle.colormode(255)

# set turtle to starting position
my_turtle.setheading(225)
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.forward(300)
my_turtle.setheading(0)
my_turtle.showturtle()
my_turtle.pendown()


def draw_dots():
    my_color = random.choice(color_list)
    my_turtle.penup()
    my_turtle.forward(50)
    my_turtle.dot(20, my_color)


def move_back():
    my_turtle.penup()
    my_turtle.left(90) 
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.left(180)


for _ in range(10):
    draw_dots()
for _ in range(9):
    move_back()
    for _ in range(10):
        draw_dots()

my_turtle.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
