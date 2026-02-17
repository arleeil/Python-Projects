#
#
#
# from turtle import Turtle,Screen
#
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color('red')
# my_screen = Screen()
#
# timmy.forward(100)
# print(timmy)
# print('Hey welcome to the turtle game:')
# move=input('Would you like the turtle to move 100 paces(y/n):').lower()
#
# if move == 'y':
#     forward = True
# else:
#     forward = False
#
# if forward is True :
#     timmy.forward(100)
# else:
#     my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
table.add_column('Pokemon Name',['Pickachu','Squirtle','Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align('left')

print(table)