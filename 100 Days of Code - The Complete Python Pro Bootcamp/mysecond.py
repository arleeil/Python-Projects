import random
print('\n--------------------Welcome to Rock, Paper , Scissors-----------------')

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
game_images=[rock, paper, scissors]
# Computer Choice
computer_options=['rock', 'paper', 'scissors']
computer_choice= random.choice(computer_options)

# User Choice
user_choice= input('\nRock , Paper, Scissors:').lower()


# Comparing
if user_choice == computer_choice:
    print("Tie , Try again !")

elif user_choice == 'rock':
    if computer_choice == 'paper':
        print(game_images[1])
        print('Computer Wins')
    elif computer_choice == 'scissors':
        print(game_images[2])
        print('User Wins')

elif user_choice == 'paper':
    if computer_choice == 'scissors':
        print(game_images[2])
        print('Computer Wins')
    elif computer_choice == 'rock':
        print(game_images[0])
        print('User Wins')

elif user_choice == 'paper':
    if computer_choice == 'rock':
        print(game_images[0])
        print('Computer Wins')
    elif computer_choice == 'paper':
        print(game_images[1])
        print('User Wins')
else:
    print('Invalid Input , Reload')

print(f'Computer Choice: {computer_choice}')





























