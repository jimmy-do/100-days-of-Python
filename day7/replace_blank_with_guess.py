# Step 2
import random_word_generator
import hangman

# TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
#  guess.


display = []

for i in random_word_generator.chosen_word:
    display.append('_')


# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]

def replace_blank_guess():
    for n in range(len(random_word_generator.chosen_word)):
        if random_word_generator.chosen_word[n] == hangman.guess:
            display[n] = hangman.guess
