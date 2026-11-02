from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffeemaker=CoffeeMaker()
money_machine=MoneyMachine()
print(menu.get_items())
user_input=input("what do you want to order sir! (espresso/latte/cappuccino): ").lower()
if (menu.find_drink(user_input)):
    if(coffeemaker.is_resource_sufficient(user_input)):
        money_machine.make_payment()