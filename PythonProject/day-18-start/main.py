import random
import turtle
from turtle import Turtle,Screen
timmy = Turtle()
screen = Screen()


# Timmy Looks
timmy.shape('turtle')
timmy.color('pink')

# Timmy Makes Square
'''for x in range(4):
    timmy.forward(100)
    timmy.right(90)'''

# Timmy Makes a Dashed Line
'''for x in range(9):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()'''
# Timmy Makes Shape
'''color = ['red', 'green', 'pink', 'orange']

def draw_shape(side_num):
    angle = 360/side_num
    for x in range(side_num):
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 11):
    draw_shape(i)
    timmy.pencolor(random.choice(color))'''

# Timmy Randomly Moves
turtle.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r, g, b)
    return rgb


'''
# Timmy Randomly Walks
nums = [ 90,0,180,270]
for x in range(100):
    timmy.pensize(10)
    timmy.pencolor(random_colour())
    timmy.speed(0)

    i = random.choice(nums)
    timmy.right(i)
    timmy.forward(20)
'''

# Timmy Draws Circle
'''timmy.speed(0)
for x in range(72):
    timmy.circle(100)
    timmy.right(5)
    timmy.pencolor(random_colour())'''

# Screen
screen.exitonclick()




















