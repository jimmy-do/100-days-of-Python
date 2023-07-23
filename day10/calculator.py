from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

num1 = input('What\'s the number? ')
operation = input('What\'s the operation? ')
num2 = input('What\'s the next number?')


