from turtle import Turtle

class Snake(): 

    def __init__(self) -> None:
        starting_postion = [(0, 0), (-20, 0), (-40, 0)]
        self.self.segments = []

        for position in starting_postion:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        # move snake
        for seg_num in range(len(self.self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
  
