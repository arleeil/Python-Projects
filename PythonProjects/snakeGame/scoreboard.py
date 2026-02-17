from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        high = open('data.txt')
        self.highest_score = high.read()
        self.penup()
        self.hideturtle()
        self.color('pink')
        self.goto(x=0, y=230)
        self.update_score()

    def update_score(self):
        self.clear()
        self.update_high_score()
        self.write(f'Score:{self.score}  Highest Score: {self.highest_score} ', align='center', font=('Arial', 10, 'normal'))

    def update_high_score(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            high = open('data.txt', mode='w')
            high.write(str(self.highest_score))





    def reset(self):
        self.score = 0
        self.update_score()
    def add_score(self):
        self.score+=1
        self.update_score()
    def game_over(self):
        self.reset()
        self.color('pink')
        self.hideturtle()
        self.goto(x=0, y=0)
        self.write(f'GAME OVER.', align='center', font=('Courier', 25, 'normal'))
        self.goto(x=0, y=-50)
        self.write(f'Your Score: {self.score} Highest Score: {self.highest_score} ', align='center', font=('Courier', 14, 'normal'))