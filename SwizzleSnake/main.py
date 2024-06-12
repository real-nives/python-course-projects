from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Swizzle Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Assigns keys to the snake's movement.
screen.listen()
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.right, 'd')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.up_score()
        snake.extend()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 240 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()