print('------------ODD OR EVEN PROGRAM ---------')
user_num = int(input('What\'s your number:'))
# Checking if the User's input is odd/even by dividing by 2
remainder = user_num %2

if remainder == 0:
    print('Your Number is in fact EVEN ')
else:
    print('Your number is ODD')