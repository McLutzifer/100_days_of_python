from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clockwise_rotation():
    tim.right(5)

def counter_clockwise_rotation():
    tim.left(5)

def reset():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise_rotation)
screen.onkey(key="d", fun=clockwise_rotation)
screen.onkey(key="c", fun=reset)
screen.exitonclick()