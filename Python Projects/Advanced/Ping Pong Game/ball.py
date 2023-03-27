from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.Xmove = 10
        self.Ymove = 10
        self.Xspeed = 0.1

    # moving ball logic

    def move(self):
        newX = self.xcor() + self.Xmove
        newY = self.ycor() + self.Ymove
        self.goto(newX, newY)

    def bounceY(self):
        self.Ymove *= -1

    def bounceX(self):
        self.Xmove *= -1
        self.Xspeed *= 0.9

    def resetPosition(self):
        self.goto(0, 0)
        self.Xspeed = 0.1
        self.bounceX()
