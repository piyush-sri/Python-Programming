from turtle import Turtle
POSITIONS =[(0, 0), ( -20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for i in POSITIONS:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(i)
            self.body.append(new_turtle)

    def move(self):
        # move snake following the head
        for s in range(len(self.body)-1, 0, -1):
            new_x = self.body[s -1].xcor()
            new_y = self.body[s - 1].ycor()
            self.body[s].goto(new_x, new_y)

        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def addsegment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def extend(self):
        #add a new segment to the snake
        self.addsegment(self.body[-1].position())

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)


    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)


    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)
