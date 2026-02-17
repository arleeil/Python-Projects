# Tip Calculator
import random




def tip_calculator():
    print('Welcome to our Tip Calculator!')
    bill = int(input('What was the total bill:'))
    percent = int(input('How much tip would you like to add? 10, 12, or 15:'))
    num_of_people = int(input('How many customers:'))

    total = ((percent/100) * bill + bill)/num_of_people
    totall = ((percent/100) * bill + bill)
    print(f'Each person should pay:$ {total} \n Total:{totall}')

# ---------------------------------------------
# Six Flags
def six_flags():
    print('Welcome To Six Flags')
    def process_payment():
        picture_bill = 0
        height = int(input('How Tall are you in cm: '))
        if height < 120:
            print('Unfortunately, You do not meet the height requirement for the rides. Our Park is available for kids')
        elif height >= 120:

            age = int(input('Age: '))
            if age >= 18:
                picture_bill+=12
                print('Adult Tickets are $12')
            elif age < 12:
                picture_bill += 5
                print('Child Tickets are $5' )
            else:
                picture_bill+= 7
                print('Child Tickets are $7 ')
            # Case - For Photos
            want_photos = input('\nPhotos are $3\nWould You like a photo:(y/n):').upper()
            if want_photos == 'Y':
                picture_bill+=3
                print(f'Total$: {picture_bill}')
            elif want_photos == 'N':
                print(f'Total:$ {picture_bill}')

    single_entry = input('Is this a single entry(y/n):')

    if single_entry == 'y':
        process_payment()
    else:

        num_of_entry = int(input('How many people are with you : '))
        for i in range(num_of_entry):
            process_payment()
            print('\n' *20)

# -----------------------
# Python Pizza
def python_pizza():
    print('Welcome tp Python Pizza Deliveries ')
    size = input('Pizza Size (S|M|L): ').upper()
    pepperoni = input('Do you want pepperoni on your pizza(y/n): ').lower()
    extra_cheese = input('Do you want extra cheese(y/n): ').lower()

    subtotal= 0
    if size == 'S':
        if pepperoni == 'y':
            subtotal+=2
        subtotal += 15
    elif size == 'M':
        subtotal += 20
        if pepperoni == 'y':
            subtotal+=3
    elif size == 'L':
        subtotal += 25
        if pepperoni == 'y':
            subtotal+=3
    if extra_cheese =='y':
        subtotal+=1
    print(f'Total$ :{subtotal}')
# Treasure Island
def treasure_land():
    print('Welcome to Treasure Island \nYour Mission is to find the treasure.')
    first_choice = input('Starting off you\'re walking there are 2 paths. Do you want to go left or right: ').lower()
    if first_choice == 'left':
        second_choice = input('Wait! There\'s some water, do you want to swim or wait: ').lower()
        if second_choice == 'wait':
            third_choice = input('Good Job! There are 3 doors (Red, Yellow, Blue): ').lower()
            if third_choice == 'red':
                print('Burned by Fire\n GAME OVER')
            elif third_choice == 'blue':
                print('Eaten by Beasts\nGame Over')
            elif third_choice == 'yellow':
                print('-----------Good Job, You came out alive---------')
        else:
            print('Attacked by trout\n Game Over')
    else:
        print('You fall into a Hole\n GAME OVER')

# Pay the Bill
def pay_that_bill():
    num_for_loop = int(input('How many names:'))
    names = []
    for x in range(num_for_loop):
        name= input('Name:')
        names.append(name)
        print('   Name Stored')

    print(f'The Bill Player:{random.choice(names)}')
    #
    # names = ['Jared', 'Henry', 'Joseph', 'Bianca', 'angie']
    # for x in names:
    #     index= random.randint(0,len(names)-1)
    # print(names[index])

# Find the highest score and manual sum
def find_high_score():
    list_of_grades = [23, 56, 89, 36, 12, 34, 78, 34, 23, 67, 12,5]
    highest_score = 0
    for y in list_of_grades:
        if y > highest_score:
            highest_score = y
    print(highest_score)

    full_sum = 0
    for x in list_of_grades:
        full_sum+=x
    print(full_sum)
    print(sum(list_of_grades))

    addition = 0
    for i in range(100):
        addition+= i
    print(addition)


# Password Generator

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print('Welcome to the Python Generator')
    letter_amount = int(input('How many letters would you like in your password:'))
    symbol_amount = int(input('How many symbols:'))
    number_amount = int(input('How many numbers:'))
    password = []
    def password_bite(amount, character_type):
        for x in range(amount):
             character = random.choice(character_type)
             password.append(character)
        return password
    password_bite(letter_amount, letters)
    password_bite(symbol_amount, symbols)
    official_password =  password_bite(number_amount, numbers)


    printable_password = ''
    random.shuffle(official_password)
    for i in official_password:
        printable_password+=i
    print(printable_password)


# To Encrypt or Decrypt
def encrypt_decrypt():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    user_wants = input('Type \'Encrypt\' or \'Decrypt\': ').lower()
    user_message = input('Type Your Message: ')
    shift_num = int(input('Type Your decided Shift Number: '))

    encoded_message=''
    decoded_message =''
    list(user_message)
    if user_wants == 'encrypt':
        for x in user_message:
            if x in alphabet:
                coded_index= alphabet.index(x) + shift_num
                coded_index%=len(alphabet)
                encoded_message += alphabet[coded_index]

        print(encoded_message)

    elif user_wants == 'decrypt':
        for x in user_message:
            if x in alphabet:
                shifted_index = alphabet.index(x) - shift_num
                shifted_index%= len(alphabet)
                decoded_message += alphabet[shifted_index]
        print(decoded_message)

# Self-Practicer Dictionaries
# Student
def class_room():
    class1 = {'Jerard Green': 78, 'Alexcia Thomas': 90, 'Leisha Isnored': 90, 'Christopehr Morgan': 100, 'Simone Clarke': 85}
    print('Welcome to Our Academic Portal! \n\n1.Update Student Grade   2.Delete Student Grade \n\n3.Add new Student and Grade   4.Print Full CLass with Grades\n\n5.Print Average For class')
    task_needed = input('\nTask Needed:')
    if task_needed == '1':
        name = input('Name:')
        grade = int(input('Grade:'))
        class1[name]= grade
        for key in class1:
            print(f'\n{key}:{class1[key]}')
        print('         Grade Updated')
    elif task_needed == '2':
        name = input('Name:')
        del class1[name]
        for key in class1:
            print(f'\n{key}:{class1[key]}')
        print('         Name Removed')
    elif task_needed == '3':
        name = input('Name:')
        grade = int(input('Grade:'))
        class1[name] = grade
        for key in class1:
            print(f'\n{key}:{class1[key]}')
        print('         Name Added')
    elif task_needed == '4':
        for key in class1:
            print(f'\n{key}:{class1[key]}')
    elif task_needed == '5':
        class_sum = 0
        for key in class1:
            class_sum+=class1[key]
        print(f'Class Average: {class_sum / len(class1)}')

# Silent Bid
def silent_bid():
    print('Welcome to Our Bid')
    bidders = {}
    another_time = 'y'
    while another_time == 'y':
        name_for_bid= input('Name for BID:')
        price_for_bid = int(input('Price for BId: '))
        another_person = input('Is there another bidder(y/n):').lower()
        bidders[name_for_bid] = price_for_bid
        if another_person == 'n':
            another_time = 'n'
            highest = 0
            winner = ''
            for key in bidders:
                if bidders[key] > highest:
                    winner = key
                    highest = bidders[key]
            print(bidders)
            print(f'The Highest Bidder is {winner} with {highest}')


        elif another_time == 'y':
            print('\n'*20)


# Day 10 - Calculator
def calculator():

    def add(n1 , n2):
        return n1 + n2
    def subtract(n1 , n2):
        return n1 - n2
    def divide(n1 , n2):
        return n1 / n2
    def multiply(n1 , n2):
        return n1 * n2

    operators = {
        multiply: '*',
        add: '+',
        divide: '/',
        subtract:'-'
    }
    result = 0
    print('Welcome to Our Calculator!')
    first_num = int(input('First Number:  '))
    print('+\n-\n*\n/')
    operation_choice = input('Pick an operation: ')
    second_num = int(input('Next number: '))

    for x in operators:
        if operation_choice == operators[x]:
            result = x(first_num,second_num)

    print(f'{first_num} {operation_choice} {second_num} = {result}')


    # Additional Calculation
    another_calc = True
    while another_calc is True:
        another_user = input(f'Type \'y\' to continue with {result}, type \'n\' to start a new calculation: ').lower()
        if another_user == 'y':
            print('+\n-\n*\n/')
            operation_choice = input('Pick an operation: ')
            second_num = int(input('Next number: '))
            for x in operators:
                if operation_choice == operators[x]:
                    result = x(result, second_num)
        elif another_user == 'n':
            another_calc = False

        print(f'\n\n{result} {operation_choice} {second_num} = {result}')

