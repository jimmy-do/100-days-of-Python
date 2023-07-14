print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

first_choice = input('You\'re at a crossroads, where do you want to go? Type "left" or "right".').lower()

# if first_choice == 'right':
#     print('Game Over.')
# else:
#     second_choice = input('You arrive at a lake. Swim or wait?').lower()
#     if second_choice == 'swim':
#         print('Game Over.')
#     else:
#         third_choice = input('You arrive at 3 doors - red, blue, and yellow. Which do you choose?').lower()
#         if third_choice == 'yellow':
#             print('You win!')
#         else:
#             print('Game Over.')

if first_choice == 'left':
    second_choice = input('You arrive at a lake. Swim or wait?').lower()
    if second_choice == 'wait':
        third_choice = input('You finally arrived at the island. There are 3 doors - blue, yellow, red. Which do you '
                             'enter?')
        if third_choice == 'yellow':
            print('You win!')
        else:
            print('Game Over.')
    else:
        print('Game Over.')
else:
    print('Game Over.')