from turtle import Turtle, Screen
import random
window = Screen()
#fixing the size of the window
window.setup(width=500, height=400)
window.title("Turtle Race")

#taking input from prompt
bet = window.textinput(title = "Snake Race Game", prompt = "Which Turtle is going to win the race? Place Your Bet."
                                                           ". By Choosing the color(red, yellow, blue, green, pink, aqua)")
#cross Check
#print(bet)
#turtle Colors
colors = ["red", "yellow", "blue", "green", "pink", "aqua"]
y_pos = [-70, -40, -10, 20, 50, 70]

is_race_on = False
#Creating Six turtle with different colors and Co-ordinates
allturtle = []
for i in range(0,6):
    new_turtle = Turtle()
    #dealing with turtle by managing its cordinates and shapes
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_pos[i])
    allturtle.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:

    for i in allturtle:
        if i.xcor() > 230:
            is_race_on = False
            win_color = i.pencolor()
            if win_color == bet:
                 print(f"You Win!!, Turtle with color {win_color} Win's the Race")
            else:
                 print(f"You Lose!!, Turtle with color {win_color} Win's the Race")

        rand_dist = random.randint(0,6)
        i.forward(rand_dist)

window.exitonclick()
