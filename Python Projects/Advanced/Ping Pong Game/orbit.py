from turtle import Turtle


class Orbit(Turtle):

    def __init__(self,pos):
        super().__init__()

        #self = Turtle()

        self.shape("square")
        self.color("white")
        # 1-20px
        # 5----100px
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def goUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def goDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)
