import turtle

import colorgram
import random
from turtle import Turtle, Screen
# Timmy Settings

timmy = Turtle()
screen = Screen()
turtle.colormode(255)
timmy.shape('turtle')
timmy.color('pink')
timmy.speed(0)
colors = colorgram.extract('image.jpg', 10)
my_colors = []

for x in colors:
   r = x.rgb.r
   g = x.rgb.g
   b = x.rgb.b
   stuff = (r,g,b)
   my_colors.append(stuff)
print(my_colors)

color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188)]

# Moving
for i in range(5):
    for x in range(10):
        timmy.color(random.choice(color_list))
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)

    timmy.setheading(0)
    timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)






screen.exitonclick()



