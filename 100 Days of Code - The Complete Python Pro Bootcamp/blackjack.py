import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# For User's Hand


game_over= 'not yet'
ready_to_play = input('Are YOu ready To Play some Black Jack!Type \'y\' or \'n :').upper()
if ready_to_play == 'Y':
    # For User's Hand
    user_hand = 0
    user_hand_sum = 0
    user_hand_display = ' '
    for x in range(1, 3):
        user_hand = str(random.choice(cards))
        user_hand_sum += int(user_hand)
        user_hand_display += user_hand + ' '

    print(f'  Your Cards: [{user_hand_display}] | Current Score: {user_hand_sum}')

    # Computer's Hand
    computer_hand = 0
    computer_hand_sum = 0
    computer_hand_display = ' '

    for x in range(1, 3):
        computer_hand = str(random.choice(cards))
        computer_hand_sum += int(computer_hand)
        computer_hand_display += computer_hand + ' '
    print(f'  Computer\'s Hand: {computer_hand}')

'''
def decision():
    if '11' in computer_hand_display and '10' in computer_hand_display:
        print('Computer Wins Black Jack')
    elif '11' in user_hand_display and '10' in computer_hand_display:
        print('You win by Black Jack')
    elif '11' in computer_hand_display and computer_hand_sum>21:
        computer_hand_sum=-10
    elif '11' in user_hand_display and user_hand_sum>21:
        user_hand_sum=-10
    elif user_hand_sum > 21:
        print('You Lose')
    elif computer_hand_sum > 21:
        print('You WIN')

decision()

# Case : User Draws another card

another_card= input('Type \'y\' to get another card and\'n\' to pass: ').lower()
if another_card == 'y':
        user_hand_display+=str(random.choice(cards)) + ' '
        user_hand_sum+=int(user_hand)
        print(f'  Your Cards: [{user_hand_display}] | Current Score: {user_hand_sum}')
        computer_hand_sum += int(computer_hand)
        decision()
elif user_hand_sum > 21:
            print('You lose!')

# Case : User Draws another card
    
elif another_card == 'n':
        if computer_hand_sum>user_hand_sum and computer_hand_sum<21:
            print('You Lose')
        else:
            print('You Win')
'''