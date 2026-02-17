from turtle import Turtle

class CreatePaddle:
     paddlee: Turtle

     def __init__(self,position):
         self.paddlee = Turtle('square')
         self.paddlee.shapesize(stretch_wid=1, stretch_len=4)
         self.paddlee.color('yellow')
         self.paddlee.penup()
         self.paddlee.goto(position)
         self.paddlee.setheading(90)
         

     def move_up(self):
         self.paddlee.forward(100)
     def move_down(self):
         self.paddlee.backward(100)
         
     