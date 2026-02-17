import turtle
from turtle import Turtle,Screen
import random
screen = Screen()
'''
def move():
    pass
def move_forward():
    tom.forward(10)
def move_backward():
    tom.backward(10)
def move_up():
    current = tom.ycor()
    tom.left((current+ 10))
def move_down():
    current = tom.ycor()
    tom.right((current + 10))
def home():
    tom.reset()
    
screen.onkey(move_forward,'w')
screen.onkey(move_backward,'s')
screen.onkey(move_up,'a')
screen.onkey(move_down,'d')
screen.onkey(home,'c')'''
is_race_on = False
screen.setup(500,400)
user_bet  = screen.textinput('Make Your bet', 'Which Turtle do you think will win, Enter a Color:')
colors = ['red', 'orange', 'yellow','green', 'blue', 'purple'  ]
all_turts = []
ycor = -100
for x in colors:
  tim = Turtle(shape='turtle')
  tim.color(x)
  tim.penup()
  ycor+=30
  all_turts.append(tim)
  tim.goto(x=-230,y=ycor)

if user_bet:
    is_race_on = True

while is_race_on is True:

    for t in all_turts:
        if t.xcor()>230:
            is_race_on = False
            winning_color = t.pencolor()
            if user_bet == winning_color:
                print(f'Great Job , {winning_color} is the winner ')
            else:
                print(f'You lose , {winning_color} is the winner ')
        rand_steps = random.randint(0,10)
        t.forward(rand_steps)

screen.exitonclick()