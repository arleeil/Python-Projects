from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(x=100, y=250)
        self.write(f'{self.l_score}', align='center', font=('Arial', 30, 'normal'))
        self.goto(x=-100, y=250)
        self.write(f'{self.r_score}', align='center', font=('Arial', 30, 'normal'))
    def l_add_score(self):
        self.l_score+=1


    def r_add_score(self):
        self.r_score += 1

