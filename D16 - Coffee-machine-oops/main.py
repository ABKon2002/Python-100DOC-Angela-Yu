from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep

machine_up = True
machine = CoffeeMaker()
menu = Menu()
bank = MoneyMachine()

while machine_up:
    sleep(3)
    order = str(input("What would you like? (espresso/latte/cappuccino/): "))
    if order == "off":
        machine_up = False
        break
    elif order == "report":
        machine.report()
        continue
    drink = menu.get_item(order)
    if drink == -1:
        print("Sorry, we don't serve that yet :(")
    elif machine.is_resource_sufficient(drink) and bank.make_payment(drink.cost):
        machine.make_coffee(drink)
    print("Please make way for the next customer..")
