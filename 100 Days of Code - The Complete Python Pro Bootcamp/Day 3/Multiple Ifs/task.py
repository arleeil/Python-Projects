print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    fname= input('First Name:')
    lname = input('Last Name:')
    if age <= 12:
        print("Child Tickets: $5.")
        bill = 5
    elif age <= 18:
        print("Teenage Tickets: $7.")
        bill = 7
    else:
        print("Adult Tickets: $12.")
        bill = 12
    want_photo = input('Would You like a photo | Type Yes / No:')
    if want_photo == 'Yes':
        bill+=3
    print(f"Your Final Total : ${bill}")

    print('---------------------Please ScreenSHOT Your Receipt---------------------')
    print(f"First Name:{fname} \nLast Name:{lname} \nOrder Number: 21373276\nPhotos: Wants Photos\nTotal:${bill}" )
    print("---------------------Thank You for Coming To Allan Park!-----------------")


else:
    print("Sorry you have to grow taller before you can ride.")
