# Day 2.3 - Your Life in Weeks

# Create a program using math and f-Strings that tells us how many days, weeks, months we have left if we live until
# 90 years old

# It will take your current age as the input and output a message with our time left in this format:

#     You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

user_years_old = int(input('How old are you? '))
years_left = 90 - user_years_old
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f'You have {days_left} days left, {weeks_left} weeks left, or {months_left} months left.')

