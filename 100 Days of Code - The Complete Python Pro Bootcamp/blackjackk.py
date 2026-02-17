import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over= 'not yet'

# User's Hand
user_hand = []
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
print(computer_hand_display)

while game_over == 'not yet':
    # Detect When computer or User has BLACKJACK
    computer_black_jack= False
    user_black_jack= False
    if '11' in computer_hand and '10' in computer_hand:
        print('You Loses')
        game_over = 'finished'
    elif '11' in user_hand and '10' in user_hand:
        print('You win ')
        game_over = 'finished'



    def is_ace(hand, hand_sum):
        if '11' in hand and hand_sum>21:
            hand_sum-=10
    is_ace(computer_hand,computer_hand_sum)
    is_ace(user_hand,user_hand_sum)
    if user_hand_sum > 21:
        game_over = 'finished'
    else:
        more_cards = False
        while more_cards is False:
            another_card = input('Type \'y\' to get another card and\'n\' to pass: ').lower()
            if another_card == 'y':
                user_hand_display += str(random.choice(cards)) + ' '
                user_hand_sum += int(user_hand)
                print(f'  Your Cards: [{user_hand_display}] | Current Score: {user_hand_sum}')
                computer_hand_sum += int(computer_hand)
            elif another_card == 'n':
                more_cards = True
                for x in range(1,17):
                    computer_hand_display += str(random.choice(cards)) + ' '
                    computer_hand_sum += int(computer_hand)
            if computer_hand_sum > user_hand_sum:
                print('----You Lose Black Jack-----')
                more_cards = True
            elif computer_hand_sum == user_hand_sum:
                print('-------------DRAW BETCH----------- ')
                more_cards = True
            else:
                print('-----------You win!-----------')
                more_cards = True



