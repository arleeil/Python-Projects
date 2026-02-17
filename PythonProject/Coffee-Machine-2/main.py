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

machine_sum = 0
def resources_sufficient(drink):
    ingredients = MENU[drink]['ingredients']
    for x in ingredients:
        if x == 'water' and ingredients[x] > resources['water']:
            print(f'Sorry, there is not enough {x}')
            return False
        elif x == 'coffee' and ingredients[x] > resources['coffee']:
            print(f'Sorry,there is not enough {x}')
            return False
        elif x == 'milk' and ingredients[x] > resources['milk']:
            print(f'Sorry,there is not enough {x}')
    return True

def process_coins(drink):
    global machine_sum
    drink_cost = MENU[drink]['cost']
    quarters = int(input('How many quarters:'))*0.25
    dimes = int(input('How many dimes:'))*0.10
    nickles = int(input('How many nickels:'))*.05
    pennies = int(input('How many pennies:'))*.01
    user_total = quarters + dimes + nickles + pennies

    if user_total == drink_cost:
        machine_sum+=drink_cost
        return True
    elif user_total > drink_cost:
        machine_sum += drink_cost
        change = user_total-drink_cost
        print(f'Here is {round(change,2)} dollars in change')
        return True
    else:
       return False

def make_coffee(drink):
    ingredients = MENU[drink]['ingredients']
    if drink != 'espresso':
        resources["water"] -= ingredients['water']
        resources['coffee'] -= ingredients['coffee']
        resources["milk"] -= ingredients['milk']
    else:
        resources["water"] -= ingredients['water']
        resources['coffee'] -= ingredients['coffee']
    print(f'Here is your {drink} beautiful')

# TODO: 1. Prompt for user-order
# TODO: 2. OFF Prompt
machine_on = True
while machine_on:
    user_order = input('What would you like? (espresso/latte/cappuccino):').lower()
    if user_order == 'off':
        machine_on = False

# TODO: 3. Print Report
    elif user_order == 'report':
        for key in resources:
            print(f'{key}: {resources[key]}')
        print(f'money: {machine_sum}')
    else:
        get_money = resources_sufficient(user_order)
        if get_money:
            successful_transaction = process_coins(user_order)
            if successful_transaction:
                make_coffee(user_order)
            else:
                print('no coffee babe')
        else:
            print('next order')


