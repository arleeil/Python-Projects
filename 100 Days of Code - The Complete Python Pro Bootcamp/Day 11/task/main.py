import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = False

while play_again is False:
    play = input(
        '------------------------Ready To Play a Game of BLACKJACK!--------------------------\n        Press enter')
    if play == '':
        play_again = False
    elif play == 'n':
        play_again = True
    user_hand = []
    computer_hand = []

    # Deal Cards
    for i in range(2):
        user_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))

    # Determine Ace rule
    user_hand_sum = sum(user_hand)
    computer_hand_sum = sum(computer_hand)

    print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
    print(f'    Computer\'s first card: {computer_hand[0]}')


    def is_ace(hand, hand_sum):
        for x in range(len(hand)):
            if hand[x] == 11:
                if hand_sum > 21:
                    hand[x]=1
                    hand_sum = sum(hand)
                else:
                    break
        return hand_sum

    user_hand_sum=is_ace(user_hand, user_hand_sum)
    computer_hand_sum = is_ace(computer_hand,computer_hand_sum)

    # Early Black Jack

    if 11 in user_hand and 10 in user_hand:
        print('----You have Won BlackJack---------')
        print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
        print(f'    Computer\'s first card: {computer_hand[0]}')
    elif 11 in computer_hand and 10 in computer_hand:
        print('----YOu have lost Black JACK------')
        print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
        print(f'    Computer\'s first card: {computer_hand[0]}')
    else:
        game_end = False
        while game_end is False:
            another_card = input('Type \'y\' to get another card, type \'n\' to pass:  ').lower()
            if another_card == 'y':
                user_hand.append(random.choice(cards))
                user_hand_sum = sum(user_hand)
                user_hand_sum = is_ace(user_hand, user_hand_sum)
                if user_hand_sum > 21:
                    print("💥 You busted! Dealer wins.")
                    game_end = True
                print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
                print(f'    Computer\'s first card: {computer_hand[0]}')
            elif  another_card == 'n':
                print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
                print(f'    Computer\'s first card: {computer_hand[0]}')
                while computer_hand_sum < 17:
                    computer_hand.append(random.choice(cards))
                    computer_hand_sum = sum(computer_hand)
                    computer_hand_sum = is_ace(computer_hand, computer_hand_sum)
                game_end = True
                if computer_hand_sum > 21:
                    print('--------BUST--------')
                    game_end = True
                    print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
                    print(f'    Computer\'s first card: {computer_hand} current score: {computer_hand_sum}')
                elif user_hand_sum > 21:
                    print('--------BUST--------')
                    game_end = True
                    print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
                    print(f'    Computer\'s first card: {computer_hand} current score: {computer_hand_sum}')
                if computer_hand_sum > user_hand_sum:
                        print('--------You Lose BlackJack----------')
                        game_end = True
                        print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
                        print(f'    Computer\'s first card: {computer_hand} current score: {computer_hand_sum}')
                elif user_hand_sum > computer_hand_sum:
                        print('---------You Win Black Jack----------')
                        game_end = True
                        print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
                        print(f'    Computer\'s first card: {computer_hand} current score: {computer_hand_sum}')
                elif user_hand_sum == computer_hand_sum:
                        print('---------You Draw--------')
                        game_end = True
                        print(f'    Your cards:{user_hand}, current score: {user_hand_sum}')
                        print(f'    Computer\'s first card: {computer_hand} current score: {computer_hand_sum}')




