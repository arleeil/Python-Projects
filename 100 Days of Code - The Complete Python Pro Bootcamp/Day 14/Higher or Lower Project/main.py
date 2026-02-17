import art
import random
import game_data



'''
the_pool = {'kim Kardashian': 365, 'Kylie Jenner': 392, 'Lee': 3, 'Kyrie': 1, 'Naymar': 231, 'Messi': 506, 'Jamie': 17, 'Billie Eillish': 125, 'Nicki Minaj': 224, 'Rihanna':149, 'Bob Marley':10, 'Viola Davis': 12 }

current_score = 0

answer_correct = True
while answer_correct is True:
    celeb1 = random.choice(list(the_pool.keys()))
    celeb2 = random.choice(list(the_pool.keys()))
    if celeb2 == celeb1:
        celeb1 = random.choice(list(the_pool.keys()))

    print(f'Current Score:{current_score}')
    print(f'celeb 1: {celeb1} celeb 2: {celeb2}')
    celeb_chosen = int(input('TYPE  1 OR 2:'))

    if celeb_chosen == 1:
        if the_pool[celeb1] > the_pool[celeb2]:
            answer_correct = True
            current_score+=1
            print('You wIN')
        else:
            answer_correct = False
            print('You Lose')
    elif celeb_chosen == 2:
        if the_pool[celeb1] < the_pool[celeb2]:
            answer_correct = True
            print('You Win ')
            current_score += 1
        else:
            answer_correct = False
            print('You lOse')
    print(' * 30)'''

celeb1 = random.choice(game_data.data)
celeb2 = random.choice(game_data.data)



current_score = 0
answer_correct = True
while answer_correct is True:
    celeb1 = celeb2
    celeb2 = random.choice(game_data.data)
    if celeb1 == celeb2:
        celeb2 = random.choice(game_data.data)

    print(art.logo)
    print(f'Current Score: {current_score}')
    print(f'Celeb 1: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}')
    print(art.vs)
    print(f'Celeb 2: {celeb2['name']}, a {celeb2['description']},from {celeb2['country']}')
    celeb_chosen = int(input('\nWho has the Most Followers(1 or 2):'))

    if celeb_chosen == 1:
            if celeb1['follower_count'] > celeb2['follower_count']:
                answer_correct = True
                current_score+=1

                print('You wIN')
                print('\n' * 30)
            else:
                answer_correct = False
                print(f'Wrong answer Current Score:{current_score}')

    elif celeb_chosen == 2:
            if celeb1['follower_count'] < celeb2['follower_count']:
                answer_correct = True


                print('You Win ')
                print('\n' * 30)
                current_score += 1
            else:
                answer_correct = False
                print(f'    \nWrong answer, High Score:{current_score}')