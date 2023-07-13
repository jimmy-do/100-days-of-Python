print("Welcome to the rollercoaster!")
height = int(input('What is your height in inches? '))

# if height <= 60:
#     print('Nah shawty')
# else:
#     print("You're good")

if height > 48:
    print('You can ride the ride!!!!')
    age = int(input('How old are you? '))
    if age < 12:
        print('Pay $5')
    elif age < 18:
        print('Pay $7')
    elif age >= 18:
        print('Pay $12')
else:
    print('You cannot ride the ride little one.')