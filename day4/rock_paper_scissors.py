import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

rock_paper_scissors = [rock, paper, scissors]

player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

print(f'You chose: {rock_paper_scissors[player_choice]}')

computer_choice = random.choice(rock_paper_scissors)
print(f'Computer chose: {computer_choice}')

if player_choice == 0:
    if computer_choice == rock:
        # print(f'Computer chose: {computer_choice}')
        print('Tie.')
    elif computer_choice == paper:
        # print(f'Computer chose: {computer_choice}')
        print('You lose.')
    elif computer_choice == scissors:
        # print(f'Computer chose: {computer_choice}')
        print('You win!')
elif player_choice == 1:
    if computer_choice == rock:
        # print(f'Computer chose: {computer_choice}')
        print('You win!')
    elif computer_choice == paper:
        # print(f'Computer chose: {computer_choice}')
        print('Tie.')
    elif computer_choice == scissors:
        # print(f'Computer chose: {computer_choice}')
        print('You lose.')
elif player_choice == 2:
    if computer_choice == rock:
        # print(f'Computer chose: {computer_choice}')
        print('You lose')
    elif computer_choice == paper:
        # print(f'Computer chose: {computer_choice}')
        print('You win!')
    elif computer_choice == scissors:
        # print(f'Computer chose: {computer_choice}')
        print('Tie.')