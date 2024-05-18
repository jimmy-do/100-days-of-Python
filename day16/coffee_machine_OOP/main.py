from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def play():
    user_prompt = input('What would you like? (espresso/latte/cappuccino)').lower()
    if user_prompt == 'report':
        money_machine.report()
        coffee_maker.report()
    elif user_prompt == 'off':
        exit('Please come back soon for more coffee! ️☕️')
    else:
        drink = menu.find_drink(user_prompt)
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        #     coffee_maker.make_coffee(drink)
        enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        if enough_ingredients:
            enough_money = money_machine.make_payment(drink.cost)
            if enough_ingredients and enough_money:
                coffee_maker.make_coffee(drink)


while True:
    play()
