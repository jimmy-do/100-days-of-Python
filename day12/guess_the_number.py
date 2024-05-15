import random

from art import logo


# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def amount_of_chances(difficulty):
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


def too_low(chance):
    chance -= 1
    if chance > 0:
        print(f'Too low. Please guess again. You have {chance} left: ')
        return chance
    else:
        exit('You ran out of lives.')


def too_high(chance):
    chance -= 1
    if chance > 0:
        print(f'Too high. Please guess again. You have {chance} left ')
        return chance
    else:
        exit('You ran out of lives.')


def play_game():
    print(logo)
    generated_num = random.randint(1, 100)
    how_difficult = input('Enter in a difficulty, Easy or Hard: ').lower()
    chances = amount_of_chances(how_difficult)
    game_over = False

    while not game_over:
        guess = int(input('Enter a guess for a number between 1 and 100: '))
        if guess < generated_num:
            chances = too_low(chances)
        elif guess > generated_num:
            chances = too_high(chances)
        elif guess == generated_num:
            print('YESSSS OMG YOU WIN!')
            game_over = True


play_game()
