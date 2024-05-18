from menu import Menu, MenuItem
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
    if user_prompt == 'off':
        exit('Please come back soon for more coffee! ️☕️')
    else:
        drink = menu.find_drink(user_prompt)
        enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        if enough_ingredients:
            money_machine.process_coins()
        enough_money = money_machine.make_payment(drink.cost)
        if enough_ingredients and enough_money:
            coffee_maker.make_coffee(drink)

while True:
    play()