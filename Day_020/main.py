from turtle import Screen, Turtle

screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my Snake Game")

starting_postion = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_postion:
    new_block = Turtle("square")
    new_block.color("white")
    new_block.goto(position)


screen.exitonclick()