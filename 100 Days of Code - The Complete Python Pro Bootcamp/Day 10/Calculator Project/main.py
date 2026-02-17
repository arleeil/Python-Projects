import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return  n1 * n2

def subtract(n1, n2):
    return  n1 - n2

def divide(n1, n2):
    return  n1 / n2

operations = {'+': add,
             '*': multiply,
             '-':subtract,
             '/': divide
}
def calculation():

    redo = True
    first_num = float(input('Number:'))
    while redo == True:

        chosen_operator = input('Choose an operator: + , -,  / , * :')
        second_num = float(input('Number:'))

        result = operations[chosen_operator](first_num, second_num)
        print(f'{first_num} {chosen_operator} {second_num} = {result}')
        another_calculation = input('Type \'y\' to continue your calculation or \'n\' to start new calculation:').lower()
        if another_calculation == 'y':
            first_num = result
        elif another_calculation == 'n':
            print('\n'*21)
            calculation()

calculation()





