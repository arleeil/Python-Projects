# wELCOME TO THE GAME
import random
print('Welcome to Our Guessing Game!')
print('I\'m thinking of a number between 1 and 100')

# Random Number
rand_num = random.randint(1, 100)

game_level = input('Easy or Hard:').lower()
def play(i):
    finished = False
    while finished is False:
        print(f'You have {i} attempts remaining')
        guess= int(input('Make a Guess:'))
        if guess < rand_num :
                    print('Too low')
        elif guess >rand_num:
                    print('Too high')
        elif guess == rand_num:
                    print('You have guessed the number')
                    finished = True
        if i == 1 :
                    finished = True
                    print('You have used all your guesses')
        i -= 1
if game_level == 'easy':
    play(10)
elif game_level == 'hard':
    play(5)



