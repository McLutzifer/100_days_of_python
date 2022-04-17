import random
from turtle import Turtle, Screen


is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]

all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

for turtle_index in range(0, 6):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(turtle)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            is_race_on = False

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
