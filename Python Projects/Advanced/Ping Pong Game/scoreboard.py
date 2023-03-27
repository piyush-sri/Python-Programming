from turtle import Screen
from orbit import Orbit
from ball import Ball
from scoreboard import Scoreboard
import time

window = Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Ping Pong Game")

#controlls animation

window.tracer(0)

rorbit = Orbit((350, 0))
lorbit = Orbit((-350, 0))
#ball object
ball = Ball()
scoreboard = Scoreboard()

window.listen()

window.onkey(rorbit.goUp, "Up")
window.onkey(rorbit.goDown, "Down")

window.onkey(lorbit.goUp, "w")
window.onkey(lorbit.goDown, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.Xspeed)
    window.update()
    ball.move()

    #collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounching nature
        ball.bounceY()

    #detect collison with rorbit
    if ball.distance(rorbit) < 50 and ball.xcor() > 320 or ball.distance(lorbit) < 50 and ball.xcor() < -320:
        ball.bounceX()

    #detect when orbit loses
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.Lpoint()

    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.Rpoint()

window.exitonclick()
