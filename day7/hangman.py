import random_word_generator
import keeping_track_of_player_lives

display = []

for i in random_word_generator.chosen_word:
    display.append('_')

chosen_word_array = []
for i in random_word_generator.chosen_word:
    chosen_word_array.append(i)

stage = len(keeping_track_of_player_lives.stages)
end_of_game = False


def replace_blank_guess():
    for n in range(len(random_word_generator.chosen_word)):
        if random_word_generator.chosen_word[n] == guess:
            display[n] = guess


def add_body_part(p):
    print(keeping_track_of_player_lives.stages[p])
    if stage == 0:
        print('You lost all your body parts. RIP.')
        end_of_game = True
        exit(0)


def if_player_won():
    if chosen_word_array == display:
        print('You win!')
        end_of_game = True
        exit(0)
    else:
        print(display)


while not end_of_game:
    if_player_won()
    guess = input('Guess a letter: ').lower()

    letter_found = random_word_generator.chosen_word.find(guess)
    if letter_found > -1:
        print('Right')
    else:
        print('Wrong')
        stage -= 1
        add_body_part(stage)
    replace_blank_guess()
