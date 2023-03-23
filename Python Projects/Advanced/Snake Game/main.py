from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
# turning off the animation for a while
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # continuing changes to be reflected onto the screen
    time.sleep(0.1)
    snake.move()

    # detect Collison with food
    if snake.body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collison with food
    if snake.body[0].xcor()>290 or snake.body[0].xcor()<-290 or snake.body[0].ycor()>290 or snake.body[0].ycor()< -290:
        game_is_on = False
        scoreboard.game_over()

    #detect collison with tail
    for s in snake.body:
        if s == snake.body[0]:
            pass
        elif snake.body[0].distance(s)<10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
