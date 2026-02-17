# def format_name(f_name,l_name):
#     first= f_name.title()
#     last= l_name.title()
#     return f'{first} {last}'
#
# formated_string = format_name('lee', 'PeArson')
#
# print(formated_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1('hello'))
print(output)