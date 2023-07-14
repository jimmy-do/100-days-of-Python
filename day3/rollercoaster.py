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
        photos = input('Do you want photos?')
        if photos == 'yes':
            print('Pay $8')
        else:
            print('Pay $5')
    elif age < 18:
        photos = input('Do you want photos?')
        if photos == 'yes':
            print('Pay $10')
        else:
            print('Pay $7')
    elif age >= 18:
        photos = input('Do you want photos?')
        if photos == 'yes':
            print('Pay $15')
        else:
            print('Pay $12')
else:
    print('You cannot ride the ride little one.')