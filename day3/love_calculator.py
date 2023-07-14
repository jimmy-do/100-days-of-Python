# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:
#     Take both people's names and check for the number of times the letters in the word TRUE occurs.
#     Then check for the number of times the letters in the word LOVE occurs.
#     Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

name_string = name1 + name2

name_string = name_string.lower()

count_t = name_string.count('t')
count_r = name_string.count('r')
count_u = name_string.count('u')
count_e1 = name_string.count('e')

count_l = name_string.count('l')
count_o = name_string.count('o')
count_v = name_string.count('v')
count_e2 = name_string.count('e')

first_digit = count_t + count_r + count_u + count_e1
second_digit = count_l + count_o + count_v + count_e2

love_score = int(str(first_digit)+str(second_digit))

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 40 < love_score < 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
