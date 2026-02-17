print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice= input('You are running and come across a 2 pathways, Do you want to go Left or Right:')
if first_choice == 'Left':
    second_choice= input('Great Choice, Now Go straight ahead. \nWAIT!! You have a lake ahead \nDo You want to wait or swim across:')
    if second_choice == 'Wait':
        third_choice = input('Good choice, Look over there.There are 3 doors. \nDo you want to go through the Red door, Blue door or the Yellow door:')
        if third_choice == 'Red':
            print('Game Over! You were burned by fire!')
        elif third_choice == 'Blue':
                print('Game Over! You were eaten by Beasts !')
        if third_choice == 'Yellow':
            print('You WIN  You have found the treasure!')
    else:
        print('Game Over, You were Attacked by trout!')
else:
    print('Game Over! You fell in a hole')



