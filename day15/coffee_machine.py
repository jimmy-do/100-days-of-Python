from menu import MENU
from resources import resources

cost = 0


def print_report():
    print(resources)


def return_cost(choice):
    global cost
    if choice == 1:
        cost = MENU['espresso']['cost']
        return cost
    elif choice == 2:
        cost = MENU['latte']['cost']
        return cost
    elif choice == 3:
        cost = MENU['cappuccino']['cost']
        return cost
    else:
        exit('You entered an invalid option.')


def deduct_ingredients(drink, ingredients):
    if drink == 1:
        ingredients['water'] -= MENU['espresso']['ingredients']['water']
        ingredients['coffee'] -= MENU['espresso']['ingredients']['coffee']
    if drink == 2:
        ingredients['water'] -= MENU['latte']['ingredients']['water']
        ingredients['milk'] -= MENU['latte']['ingredients']['milk']
        ingredients['coffee'] -= MENU['latte']['ingredients']['coffee']
    if drink == 3:
        ingredients['water'] -= MENU['cappuccino']['ingredients']['water']
        ingredients['milk'] -= MENU['cappuccino']['ingredients']['milk']
        ingredients['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
    if drink == 4:
        return
    for i in ingredients:
        return ingredients[i]


def calculate(cost_of_drink, menu_option, ingredients):
    coins_total = 0
    quarters = int(input('How many quarters? '))
    coins_total += quarters * .25
    dimes = int(input('How many dimes? '))
    coins_total += dimes * .1
    nickels = int(input('How many nickels? '))
    coins_total += nickels * .05
    difference = cost_of_drink - coins_total
    if deduct_ingredients(menu_option, ingredients) < 0:
        exit('Sorry no more ingredients.')
    if difference < 0:
        print(f"Here is your change: {'{:.2f}'.format(abs(difference))}")
        if menu_option == 1:
            print('Enjoy your espresso!')
        elif menu_option == 2:
            print('Enjoy your latte!')
        elif menu_option == 3:
            print('Enjoy your cappuccino!')
    elif difference > 0:
        print('Not enough money. Money refunded.')


def play():
    user_prompt = int(input('What would you like?\n1) Espresso\n2) Latte\n3) Cappuccino?\n4) Report\n5) Exit '))
    if user_prompt == 4:
        print_report()
        return
    else:
        calculate(return_cost(user_prompt), user_prompt, resources)


while True:
    play()
