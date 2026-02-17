import random

myName = 'Lee Pearson'
myNumber = 3254635
isVirgin = True
family =['Kyrie', 'Simone', 'Kaylee', 'Christoper']
boyfriend= {'name': 'Chris', 'age':21, 'shoe_size': 11}
responses = ['Yes', 'NO']

print('Welcome to crystal bawl')
user_input = input('Type shake:')

if user_input:
    print(random.choice(responses))