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

num1 = int(input('What\'s the number? '))
for key in operators:
    print(key)
operation = input('What\'s the operation? ')
num2 = int(input('What\'s the next number? '))

calculate = operators[operation]
answer = calculate(num1, num2)

print(f'{num1} {operation} {num2} = {answer}')
