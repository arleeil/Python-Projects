import math
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO:1. Prompt User For Coffee Choice
profit = 0
def check_res(water, milk, coffee):
    if resources['water'] < water :
        print('Sorry there is not enough water')
        return True

    elif resources['milk'] < milk:
        print('Sorry there is not enough milk')
        return True

    elif resources['coffee'] < coffee:
        print('Sorry there is not enough coffee')
        return True
    else:
        return False


def make_coffee(water,milk,coffee):
        water_left = resources['water'] - water
        milk_left = resources['milk'] - milk
        coffee_left = resources['coffee'] - coffee
        resources['water'] = water_left
        resources['milk'] = milk_left
        resources['coffee'] = coffee_left
        print(f'Here is your Coffee!')
        return False

def process_coins(cost):
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    pennie = 0.01

    print('Please insert coins.')
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickels: '))
    pennies = int(input('How many pennies: '))


    total = (quarter *quarters) + (dimes*dime) + (nickles*nickle) + (pennies*pennie)
    if total > cost:
        sub = total - cost
        change = math.ceil(sub * 100) / 100
        print(f'Here is ${change} dollars in change.')
    elif total == cost:
        print('Perfect!')
    elif total < cost:
        print('Sorry That\'s not enough money | Money Refunded')
        return 0
    return cost




order_up = False
while order_up is False:
    user_want = input('\nWhat would you like?(espresso/latte/cappuccino):  ').lower()

    if user_want == 'report':
        # Print Report
        for x in resources:
            if x == 'coffee':
                print(f'{x.capitalize()}: {resources[x]}g')
            else:
                print(f'{x.capitalize()}: {resources[x]}ml')
        print(f'Money: ${profit}')

    elif user_want == 'espresso':
            available = check_res(50, 0, 18)
            if  available is False:
                final_total = process_coins(MENU['espresso']['cost'])
                if final_total == MENU['espresso']['cost']:
                    make_coffee(50,0,18)
                    profit+=final_total


    elif user_want == 'latte':
        available = check_res(250, 150, 24)
        if available is False:
            final_total = process_coins(MENU['latte']['cost'])
            if final_total == MENU['latte']['cost']:
                make_coffee(250, 150, 24)
                profit += final_total


    elif user_want == 'cappuccino':
        available = check_res(250, 100, 24)
        if available is False:
            final_total = process_coins(MENU['cappuccino']['cost'])
            if final_total == MENU['cappuccino']['cost']:
                make_coffee(250, 100, 24)
                profit += final_total

    elif user_want == 'off':
        order_up = True




