from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("DarkGoldenrod")

for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


screen = Screen()
screen.exitonclick()
