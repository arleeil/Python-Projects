ingredients ={
    'cappuccino':{
        'milk':60,
        'coffee':10,
        'water':0,
        'cost':{
            5
        }
    },
    'latte':{
        'milk' :0,
        'coffee':10,
        'water':50,
        'cost':{
            3.50
        }
    },
    'espresso':{
        'milk':0,
        'coffee':20,
        'water':40,
        'cost':{
            3
        }
    },
    'Resources':{
        'milk':500,
        'water':500,
        'coffee':500
    }
}
milk = 500
water =500
coffee = 500
# Welcome to The Coffee Machine Project
print('-------------Menu----------------')

def sufficient_resources(drink):
     for item , amount in ingredients[drink].items():
         if amount > ingredients['Resources'].get(item, 0):
             return False
     return True




user_input = input('What would ou like to Order Today Beautiful: ')

if user_input == 'off':
    print('Machine Powering Off....')
elif user_input == 'report':
    for x in ingredients['Resources']:
        print(f'{x.capitalize()} = {ingredients['Resources'][x]}')
elif user_input == 'cappuccino':
    print('Making Your Coffee...')
    print(sufficient_resources(user_input))

