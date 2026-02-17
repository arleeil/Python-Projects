import random

random_number = random.randint(1,101)

game_type = input('Easy or Hard:').lower()

print(random_number)


if game_type == 'easy':

    print('You have 10 attempts left')
    game_end = False
    tries = 10
    while game_end is False:
        user_guess = int(input('Guess a Number Hoe: '))
        if user_guess < random_number:
            tries -= 1
            print('Too Low')
            print(f'You have {tries} attempts left')
        elif user_guess > random_number:
            tries -= 1
            print('Too High')
            f'You have {tries} attempts left'
        elif tries == 0:
            game_end = True
            print('Game End')
        elif user_guess == random_number:
            print(f'You got it ,{random_number}')
            game_end = True
elif game_type == 'hard':
        print('You have 5 attempts left')
        game_end = False
        tries = 5
        while game_end is False:
            user_guess = int(input('Guess a Number Hoe: '))
            if tries == 0:
                game_end = True
                print('Game End')
            elif user_guess < random_number:
                tries -= 1
                print('Too Low')
                print(f'You have {tries} attempts left')
            elif user_guess > random_number:
                tries -= 1
                print('Too High')
                f'You have {tries} attempts left'

            elif user_guess == random_number:
                print(f'You got it ,{random_number}')
                game_end = True

