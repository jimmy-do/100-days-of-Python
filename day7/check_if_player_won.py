# Step 3
import random_word_generator
import replace_blank_with_guess
import hangman

chosen_word_array = []
for i in random_word_generator.chosen_word:
    chosen_word_array.append(i)


def if_player_won():
    if chosen_word_array == replace_blank_with_guess.display:
        hangman.end_of_game = True
        print('You win!')
        exit(0)
    else:
        print(replace_blank_with_guess.display)
