from art import logo
print(logo)

def main_prog():
    user_exit = False
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    while not user_exit:
        if shift > len(alphabet):
            shift = int(input('Please try again, shift number too large (press 0 to exit): '))
            if shift == 0:
                print(f'You entered {shift}. Exiting program.')
                exit(0)
        elif shift < 0:
            shift = int(input('Please input a valid response. Please try again. (press 0 to exit): '))
            if shift == 0:
                print(f'You entered {shift}. Exiting program.')
                exit(0)
        else:
            user_exit = True

    caesar(direction, text, shift, alphabet)
    restart_program()


# def encrypt(word, shift_amount):
#     for letter in word:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         word = word.replace(letter, alphabet[new_position])
#     return word
#
#
# def decrypt(word, shift_amount):
#     for letter in word:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         word = word.replace(letter, alphabet[new_position])
#     return word
#
#


# ****** Lack of clear parameters/arguments (variable 'shadowing') leads to unintended outputs from functions
# def caesar(option, word, shift_amount, abc):
#     caesar_cipher = ''
#     for letter in word:
#         if option == 'encode':
#             position = abc.index(letter)
#             new_position = position + shift_amount
#             caesar_cipher += abc[new_position]
#         elif option == 'decode':
#             position = abc.index(letter)
#             new_position = position - shift_amount
#             caesar_cipher += abc[new_position]
#         else:
#             exit(0)
#     print(caesar_cipher)

def caesar(option, word, shift_amount, abc):
    caesar_cipher = []
    word_list = list(word)
    for letter in word_list:
        if option == 'encode':
            position = abc.index(letter)
            new_position = position + shift_amount
            caesar_cipher.append(abc[new_position])
        elif option == 'decode':
            position = abc.index(letter)
            new_position = position - shift_amount
            caesar_cipher.append(abc[new_position])
        else:
            exit(0)
    print(''.join(caesar_cipher))


def restart_program():
    restart = input('Do you want to restart the program? Y or N?').lower()
    if restart == 'y':
        main_prog()
    else:
        exit(0)


main_prog()
