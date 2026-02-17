# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import  art
print(art.logo)

overall_storage =[]

redo ='yes'
while redo== 'yes':
    # Bidders Info
    user_name = input('Name:')
    user_bid = int(input('Bid Amount:'))
    bid_storage = {}

    # Compile each bidder's information
    bid_storage[user_name] = user_bid
    overall_storage.append(bid_storage)

    # Redo Program
    another_bid = input('Is There another Player? Type Y or N:').upper()
    if another_bid == 'Y':
        print('\n' * 30)
    elif another_bid =='N':
        redo='no'

highest_bid=0
winner =''

for x in overall_storage:
    for y in x:
        if x[y] > highest_bid:
            winner=y
            highest_bid = x[y]
print(f'Winner of this silent Bid:{winner}')