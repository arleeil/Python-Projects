from turtle import Turtle

class Ball(Turtle):
     def __init__(self):

         super().__init__()
         self.shapesize(stretch_wid=1, stretch_len=1)
         self.goto(x=0, y=0)
         self.color('orange')
         self.shape('circle')
         self.move_x = 1
         self.move_y =  1
     def ball_move(self):

         self.penup()
         new_x = self.xcor()+ self.move_x
         new_y = self.ycor() + self.move_y
         self.goto(new_x, new_y)
     def bounce_y(self):
         self.move_y *= -1

     def bounce_x(self):
         self.move_x *= -1
     def reset_positions(self):
         self.goto(0,0)
         self.bounce_x()




