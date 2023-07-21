alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

user_exit = False


def exit_program():
    if user_exit:
        exit(0)


while not user_exit:
    if shift > len(alphabet):
        user_input = int(input('Please try again, shift number too large (press 0 to exit): '))
        if shift == 0:
            exit_program()
    else:
        break


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


def caesar(word, shift_amount):
    for letter in word:
        if direction == 'encode':
            position = alphabet.index(letter)
            new_position = position + shift_amount
            word = word.replace(letter, alphabet[new_position])
        elif direction == 'decode':
            position = alphabet.index(letter)
            new_position = position - shift_amount
            word = word.replace(letter, alphabet[new_position])
    return word


print(f'{caesar(text, shift)}')
