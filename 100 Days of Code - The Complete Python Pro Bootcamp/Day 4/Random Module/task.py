import random

# Printing a random decimal

# random_float= random.random()*10
# print(random_float)


# Printing a random number


random_integer  = random.randint(1, 2)


user_choice=input('You Win or Die!\nHeads Or Tails:')
# -----------Computer Choice----------
if random_integer ==1:
    print("Heads")

elif random_integer ==2:
    print("Tails")
# ---------Computer Choice----------

# Function for Who Wins
if user_choice == "Heads" and random_integer == 1:
    print('You live to guess another DAY!')
elif user_choice == "Tails" and random_integer == 2:
    print('You live to guess another DAY!')
else:
    print('Say Good Bye to Your Mom')









