import random
print('\n-----------------WELCOME TO WHO PAYS THE BILL------------')

user_names =[]

is_finished = False

while not is_finished:
    user_name = input('Type the name of your Friend:')
    user_finished= input('Is that the last name type Y or N:')
    user_names.append(user_name)
    if user_finished == 'Y':
        is_finished=True

print(random.choice(user_names))
































