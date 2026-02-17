from turtle import Turtle,Screen
from paddle import CreatePaddle
from ball import Ball
from score import Score
import time
screen= Screen()
screen.bgcolor('black')
screen.title('PUG GAME')
screen.screensize(800,500)
screen.tracer(0)


r_paddle = CreatePaddle((320 , 0))
l_paddle = CreatePaddle((-320 , 0))
score = Score()
ball = Ball()

screen.update()



screen.listen()
screen.onkey(key='Up', fun=r_paddle.move_up)
screen.onkey(key='Down',fun=r_paddle.move_down)
screen.onkey(key='w', fun=l_paddle.move_up)
screen.onkey(key='s',fun=l_paddle.move_down)

game_on = True
while game_on:
    screen.update()
    ball.ball_move()

    # Detect Collision with Wall
    if ball.ycor() < -300 or ball.ycor() > 300:
        ball.bounce_y()

    # Detect if ball hit paddle
    if ball.distance(r_paddle.paddlee) < 50 and ball.xcor() > 280 or ball.distance(l_paddle.paddlee) < 50 and ball.xcor() < -280:
        print('Hitt')
        ball.bounce_x()

    if ball.xcor() < -400:
        ball.reset_positions()
        score.l_add_score()
        score.update_score()
    elif ball.xcor() >400:
        ball.reset_positions()
        score.r_add_score()
        score.update_score()

screen.update()






screen.exitonclick()