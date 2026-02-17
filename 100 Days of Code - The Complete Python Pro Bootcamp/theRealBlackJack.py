# My Black Jack Project.
import random


start_game = input('Do you want to play Black Jack (y/n):  ').lower()
user_hand = []
computer_hand = []

'''game_on = True

    # Dealing Cards

user_hand = []
computer_hand = []

for x in range(2):
        rand_card = random.choice(cards)
        user_hand.append(rand_card)
        user_hand_sum = sum(user_hand)
for y in range(2):
            rand_card = random.choice(cards)
            computer_hand.append(rand_card)
            computer_hand_sum = sum(computer_hand)
print(f'  Your cards:{user_hand}, current score:{user_hand_sum} ')
print(f'  Computer\'s first card: {computer_hand[0]}')
while game_on is True:
    # Checking Ace
    for o in user_hand:
        if o == 11:
            if user_hand_sum >21:
                o = 1
    for o in computer_hand:
        if o == 11:
            if computer_hand_sum >21:
                o = 1





    # Detect when computer has blackjack
    if 11 in computer_hand and 10 in computer_hand:
        if computer_hand_sum == 21:
            print('Computer Hit Black Jack. You Lost')
            game_on = False
    elif 11 in user_hand and 10 in user_hand:
        if user_hand_sum == 21:
            print('Congrats You hit black JACK')
            game_on = False
    elif user_hand_sum > 21:
        print('Game Ended, You bursted ')
        game_on = False
    else:
        another_card = input('Do you want another card(y/n):  ').lower()

        if another_card == 'y':
            add_card = random.choice(cards)
            user_hand.append(add_card)
            print(f'  Your cards:{user_hand}, current score:{user_hand_sum} ')
            print(f'  Computer\'s first card: {computer_hand[0]}')

'''
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(hand):
    card_sum = sum(hand)
    return card_sum


for _ in range(2):
    card = deal_card()
    user_hand.append(card)
for _ in range(2):
    card = deal_card()
    computer_hand.append(card)

user_hand_sum = calculate_score(user_hand)
computer_hand_sum = calculate_score(computer_hand)


game_on = True
while game_on is True:
    for x in range(len(user_hand)):
         if user_hand[x] == 11 and user_hand_sum > 21:
             user_hand[x] = 1
             user_hand_sum = calculate_score(user_hand)

    for x in computer_hand:
         if x == 11 and computer_hand_sum > 21:
             x = 1
             computer_hand_sum = calculate_score(computer_hand)



    print(f'  Your cards:{user_hand}, current score: {user_hand_sum} ')
    print(f'  Computer\'s first card: {computer_hand[0]}')

    if computer_hand_sum == 21:
        if 11 in computer_hand and 10 in computer_hand:
            print('You Lost! Computer Hit BlACK jACK')
            game_on = False
        else:
            print('You Lost! Computer Hit BlACK jACK')
            game_on = False
    elif user_hand_sum == 21:
        if 11 in user_hand and 10 in user_hand:
            print('YOu hIt early Black Jack!')
            game_on = False
        else :
            print('YOu hIt early Black Jack!')
            game_on = False
    elif user_hand_sum > 21:
       print('Game Over , You went over!')
       game_on = False
    else:
        another_card = input('Do you want to draw another card(y/n):  ').lower()

        if another_card == 'y':
            add_card = deal_card()
            user_hand.append(add_card)
            user_hand_sum+=add_card
        elif another_card == 'n':
            while computer_hand_sum < 16:
                add_card = deal_card()
                computer_hand.append(add_card)
                computer_hand_sum+= add_card

                game_on = False
                # Last Results
                if computer_hand_sum > user_hand_sum :
                    print('You LOSE!' )
                elif computer_hand_sum < user_hand_sum:
                    print('YOU WIN!')
                elif computer_hand_sum == user_hand_sum:
                    print('DRAW HOE')
                elif computer_hand_sum <= 21:
                    print('You Win')
                print(f'\n\nFinal Scores :\n  Your cards:{user_hand}, current score: {user_hand_sum}'  )
                print(f'  Computer\'s first card: {computer_hand} current score: {computer_hand_sum}')

