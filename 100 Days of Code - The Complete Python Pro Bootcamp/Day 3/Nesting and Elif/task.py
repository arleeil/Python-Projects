print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input('How old are you:'))
    if age <= 12:
        print('Your total is $5.00')
    elif age <=18:
        print('Your total is $8.00')
    elif age > 18 :
        print('Your total is $12.00')
else:
    print("Sorry you have to grow taller before you can ride.")
