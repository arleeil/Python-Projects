import random

from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password=[]
user_letter= int(input('\nHow many letters would you like in your password:'))
user_numbers= int(input('How many numbers would you like in your password:'))
user_symbols= int(input('How many symbols would you like in your password:'))

for i in range(user_letter):
    password.append(random.choice(letters))
for i in range(user_numbers):
    password.append(random.choice(numbers))
for i in range(user_symbols):
    password.append(random.choice(symbols))

final_password=''

random.shuffle(password)

for i in password:
    final_password+=i

print(final_password)



