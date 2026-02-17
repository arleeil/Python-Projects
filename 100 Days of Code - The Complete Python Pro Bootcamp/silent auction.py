print('Welcome to Our Silent Auction')

pizza=[{'Lee': 234}, {'Alex': 789}, {'Stacey ': 66}]


winner=''
highest_bid=0
for x in pizza:
    for y in x:
        if x[y] > highest_bid:
            winner=y
            highest_bid = x[y]

print(highest_bid)
print(winner)