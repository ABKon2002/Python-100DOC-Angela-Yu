from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

short_forms = {
    'e' : 'espresso',
    'l' : 'latte',
    'c' : 'cappuccino'
}


def print_report(res, money):
    print("\n******REPORT******")
    print(f"Water : {res['water']} mL")
    print(f"Milk : {res['milk']} mL")
    print(f"Coffee : {res['coffee']} g")
    print(f"Money : $ {money}")
    print()


def ask_payment(drink):
    cost = MENU[drink]['cost']
    print(f"Please pay $ {cost} to proceed...")
    print("We accept quarters, dimes, nickels and pennies.")


def resources_sufficient(drink):
    content = MENU[drink]['ingredients']
    for ingredient in content:
        if content[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient} for {drink}.")
            return False
    return True


def process_payment(choice, paid):
    cost = MENU[choice]['cost']
    global balance
    if paid > cost:
        change = paid - cost
        change = round(change, 2)
        print(f"Payment Successful, Here is $ {change} dollars in change.")
        print("Please wait for your drink...")
        balance += cost
        sleep(3)
        return True
    elif paid == cost:
        print(f"Payment Successful, Please wait for your drink...")
        balance += cost
        sleep(3)
        return True
    else:
        print(f"Sorry that is not enough for {choice}, Please pay {cost}!")
        print("Payment unsuccessful. Make way for the next customer...")
        sleep(3)
        return False


def make_coffee(drink):
    recipe = MENU[drink]['ingredients']
    for ingredient in recipe:
        resources[ingredient] -= recipe[ingredient]
    print(f"Here is your {drink}! Enjoy")
    print()
    sleep(2)


balance = 0

while True:
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso or 'e'/ latte or 'l' / cappuccino or 'c'): ").lower()

    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == 'off':
        print("Shutting down...")
        sleep(2)
        break

    # 3. Print report.
    elif choice == 'report':
        print_report(resources, balance)
        continue

    elif choice in ['e', 'c', 'l']:
        choice = short_forms[choice]

    if choice not in ['latte', 'espresso', 'cappuccino']:
        print(f"Sorry, {choice} is not in our menu.")
        print("Make way for the next order...")
        sleep(2)
        continue

    # 4. Check resources sufficient?
    if not resources_sufficient(choice):
        continue

    # 5. Process coins.
    ask_payment(choice)
    quarters = int(input("No of quarters ($ 0.25): "))
    dimes = int(input("No of dimes ($ 0.10): "))
    nickels = int(input("No of nickels ($ 0.05): "))
    pennies = int(input("No of pennies ($ 0.01): "))

    paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    # 6. Check transaction successful?
    if not process_payment(choice, paid):
        continue

    # 7. Make Coffee.
    make_coffee(choice)
