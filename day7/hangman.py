import random_word_generator
import replace_blank_with_guess
import check_if_player_won

end_of_game = False

while not end_of_game:

    check_if_player_won.if_player_won()
    guess = input('Guess a letter: ').lower()
    letter_found = random_word_generator.chosen_word.find(guess)
    if letter_found > -1:
        print('Right')
    else:
        print('Wrong')

    replace_blank_with_guess.replace_blank_guess()


