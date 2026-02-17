import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
another_game = False


def ace(hand, hand_sum):
    for y in range(len(hand)):
        if hand[y] == 11 and hand_sum > 21:
            hand[y] = 1
            hand_sum = sum(hand)
    return hand_sum
while another_game is False:
    user_hand = []
    computer_hand =[]
    # Deal CARDS
    for x in range(1,3):
        user_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
    user_hand_sum = sum(user_hand)
    computer_hand_sum= sum(computer_hand)
    print(f'  Your Cards: {user_hand} | Current Score: {user_hand_sum}')
    print(f'  Computer\'s First Hand: {computer_hand[0]} ')

    # Check if Game needs to end
    if 11 in user_hand and 10 in user_hand:
        print('-----------User wins BLack JACk------------- ')
        another_game = True
    elif 11 in computer_hand and 10 in computer_hand:
        print('-----------User loses BLack JACk------------')
        another_game = True




    computer_hand_sum= ace(computer_hand,computer_hand_sum)
    user_hand_sum= ace(user_hand, user_hand_sum)

    # Case - User Draws for Another Card
    game_end = False
    while game_end is False:
        another_card = input('Type \'y\' to get another card and\'n\' to pass: ').lower()
        if another_card == 'y':
            user_hand.append(random.choice(cards))
            computer_hand_sum = ace(computer_hand, computer_hand_sum)
            user_hand_sum = ace(user_hand, user_hand_sum)
            print(f'  Your Cards: {user_hand} | Current Score: {user_hand_sum}')
            print(f'  Computer\'s : {computer_hand} Score: {computer_hand_sum}')
            if user_hand_sum > 21 or computer_hand_sum > 21:
                game_end = True
        # Computer Deals
        elif another_card == 'n':
            while computer_hand_sum < 16:
                computer_hand.append(random.choice(cards))
                computer_hand_sum = ace(computer_hand, computer_hand_sum)
                user_hand_sum = ace(user_hand, user_hand_sum)
            game_end=True

    if user_hand_sum == 21:
        print('-----------User wins BLack JACk------------- ')
    elif computer_hand_sum == 21:
        print('-----------User loses BLack JACk------------')
    elif computer_hand_sum >21:
        print('BUST HOE')
    elif user_hand_sum >21:
        print('BUST hOW')
    elif computer_hand_sum>user_hand_sum :
        print('YOU LOSE----')
        print(f'  Your Cards: {user_hand} | Current Score: {user_hand_sum}')
        print(f'  Computer\'s Hand: {computer_hand} Score: {computer_hand_sum} ')
    elif user_hand_sum>computer_hand_sum:
        print('YOU WIN----------')
        print(f'  Your Cards: {user_hand} | Current Score: {user_hand_sum}')
        print(f'  Computer\'s Hand: {computer_hand} Score: {computer_hand_sum}')
    elif computer_hand_sum == user_hand_sum:
        print('DRAW')
        print(f'  Your Cards: {user_hand} | Current Score: {user_hand_sum}')
        print(f'  Computer\'s Hand: {computer_hand} Score: {computer_hand_sum}')



