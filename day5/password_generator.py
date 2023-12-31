# #Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Eazy

# random_letters = ''
# random_symbols = ''
# random_numbers = ''
#
# for x in range(nr_letters):
#     random_letters += random.choice(letters)
#
# for y in range(nr_symbols):
#     random_symbols += random.choice(symbols)
#
# for z in range(nr_numbers):
#     random_numbers += random.choice(numbers)
#
# password = random_letters + random_symbols + random_numbers
#
# print(password)

# Hard

random_letters = ''
random_symbols = ''
random_numbers = ''

for x in range(nr_letters):
    random_letters += random.choice(letters)

for y in range(nr_symbols):
    random_symbols += random.choice(symbols)

for z in range(nr_numbers):
    random_numbers += random.choice(numbers)

password = f'{random_letters}{random_symbols}{random_numbers}'
shuffled_password = []

for p in password:
    shuffled_password.append(p)

random.shuffle(shuffled_password)

for s in shuffled_password:
    password += s

print(password)
# print(random.shuffle(shuffled_password)) # shuffles in place, will not work -> nonexistent output
