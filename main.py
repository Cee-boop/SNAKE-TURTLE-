from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE')
screen.tracer(False)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# key maps:
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

# game logic:
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food:
    if snake.head.distance(food) < 14:
        food.refresh()
        scoreboard.increment_score()
        snake.extend()

    # detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 \
    or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
