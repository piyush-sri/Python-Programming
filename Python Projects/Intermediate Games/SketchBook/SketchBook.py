from turtle import Turtle, Screen
orbit = Turtle()
window = Screen()
orbit.pensize(10)
orbit.pencolor("red")
orbit.shape("turtle")
def move_forward():
    orbit.forward(10)

def move_backward():
    orbit.backward(10)

def move_left():
   new_heading = orbit.heading()+10
   orbit.setheading(new_heading)

def move_right():
    new_heading = orbit.heading() - 10
    orbit.setheading(new_heading)

def clear():
    orbit.clear()
    orbit.penup()
    orbit.home()
    orbit.pendown()

#Event Listener
window.listen()
window.onkey(move_forward,"w")
window.onkey(move_backward,"s")
window.onkey(move_left,"a")
window.onkey(move_right,"d")
window.onkey(clear,"c")
window.exitonclick()
