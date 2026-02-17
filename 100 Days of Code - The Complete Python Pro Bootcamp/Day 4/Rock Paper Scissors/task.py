import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('---------------Our Python Game -----------------')
print('----------Welcome to Rock , Paper Scissors-------')
user_choice = input('Chose - "Rock"  "Paper"  "Scissors":')

# Computer Choice

choices=['Rock', 'Paper', 'Scissors']
computer_choice= random.choice(choices)

# Function for Decision

if user_choice == computer_choice:
    print('DRAW---------You\'re Going to Have to Try Again. ')
#     For Rock--------
elif user_choice=='Rock':
    print(rock)
    if computer_choice == 'Scissors':
        print('Computer\'s Choice:')
        print(scissors)
        print('Good Call , You Win!!')
    if computer_choice== 'Paper':
        print('Computer\'s Choice:')
        print(paper)

        print('Silly Loser , Better Luck Next Time!')

#      For Scissors-----
elif user_choice == 'Scissors':
    print(scissors)
    if computer_choice== 'Paper':
        print('Computer\'s Choice:')
        print(paper)
        print('Good Call , You Win!!')
    if computer_choice== 'Rock':
        print('Computer\'s Choice:')
        print(rock)
        print('Silly Loser , Better Luck Next Time!')

#     For Paper------
elif user_choice == 'Paper':
    print(paper)
    if computer_choice == 'Rock':
        print('Computer\'s Choice:')
        print(rock)
        print('Good Call , You Win!!')
    if computer_choice == 'Scissors':
        print('Computer\'s Choice:')
        print(scissors)
        print('Silly Loser , Better Luck Next Time!')
else:
    print('Are you Again , Be sure to type the right thing!')






