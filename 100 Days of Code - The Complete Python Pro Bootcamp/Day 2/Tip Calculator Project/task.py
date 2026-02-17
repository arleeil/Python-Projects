# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

print('Welcome to the tip calculator!')

bill= float(input('What was the total bill:'))
tip=int(input('How much tip would you like to give (10, 12, 15):'))
num_people=int(input('How many people to split the bill:'))
subtotal=( bill/7)+(tip/100*bill)/7
total = round(subtotal, 2)
print(f'Each person should pay: {total}')


