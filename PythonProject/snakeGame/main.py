from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(500, 500)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with Food
    if snake.head.distance(food) < 15: 
        food.refresh()
        snake.extend()
        score.add_score()


    # Detect Collision with Food
    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or  snake.head.ycor() < -245:
        snake.reset()
        score.reset()

    # Collision with Tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset()
            score.reset()



screen.exitonclick()