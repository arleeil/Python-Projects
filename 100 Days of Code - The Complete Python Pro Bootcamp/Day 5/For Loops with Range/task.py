# for num in range(1, 11, 2):
#     print(num)
#
# summ = 0
# for num in range(1,101):
#     summ+=num
# print(summ)

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)



