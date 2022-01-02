from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
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
    screen.update()
    time.sleep(0.07)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh_food()
        scoreboard.update_score()
        snake.extend()

    # Detect when snake hits the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.abort()

    # Detect collision with tail
    for snek in snake.snakes[1:]:
        if snake.head.distance(snek) < 10:
            game_is_on = False
            scoreboard.abort()


screen.exitonclick()
