from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Lower float = faster ball.
BALL_SPEED = .015

screen = Screen()
screen.setup(width=1200, height=900)
screen.bgcolor('black')
screen.title('Peter Pong')
screen.tracer(0)

scoreboard = Scoreboard()
paddle_1 = Paddle((-550, 0))
paddle_2 = Paddle((550, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_1.move_paddle_up, 'w')
screen.onkey(paddle_1.move_paddle_down, 's')
screen.onkey(paddle_2.move_paddle_up, 'i')
screen.onkey(paddle_2.move_paddle_down, 'k')

game_is_on = True

while game_is_on:
    time.sleep(BALL_SPEED)
    screen.update()
    ball.move_forward()
    #Detect collision with top or bottom of screen.
    if ball.ycor() > 435 or ball.ycor() < -425:
        ball.bounce_y()
    #Detect collision with paddles.
    if ball.distance(paddle_1) < 65 and ball.xcor() < -525 or ball.distance(paddle_2) < 65 and ball.xcor() > 525:
        ball.bounce_x()
    #Detect ball out of bounds. Game Over.
    elif ball.xcor() > 582 or ball.xcor() < -592:
        if ball.xcor() > 0:
            scoreboard.p1_point()
        else:
            scoreboard.p2_point()
        if scoreboard.p1_score > 4 or scoreboard.p2_score > 4:
            if scoreboard.p1_score > scoreboard.p2_score:
                scoreboard.winner('Player 1')
            else:
                scoreboard.winner('Player 2')
            break
        ball.reset_position()
        paddle_1.reset_position()
        paddle_2.reset_position()

screen.exitonclick()