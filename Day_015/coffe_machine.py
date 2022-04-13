starting_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

starting_profit = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def insert_money(choice):
    print("please insert coins")
    pennies = int(input("How many pennies?: >> "))
    dimes = int(input("How many dimes?: >> "))
    nickels = int(input("How many nickels?: >> "))
    quarters = int(input("How many quarters?: >> "))
    total = pennies * 0.01 + dimes * 0.05 + nickels * 0.1 + quarters * 0.25

    if total < MENU[choice]["cost"]:
        total = 0
        return total

    excess_money = total - MENU[choice]["cost"]
    print(f"Here is ${excess_money} in change")
    total -= excess_money
    return total


def check_ingredients(coffee_choice, present_resources):
    for ingredient in ("water", "milk", "coffee"):
        if MENU[coffee_choice]["ingredients"][ingredient] > present_resources[ingredient]:
            print(f"sorry, there is not enough {ingredient}")
            return False
    return True


def make_coffee(choice, resources):
    for ingredient in MENU[choice]["ingredients"]:
        resources[ingredient] -= MENU[choice]["ingredients"][ingredient]
    print(f"Here is your {choice}")


def main(money, resources):
    status = "ON"
    while status == "ON":
        choice = input("What would you like? (espresso/latte/cappuccino): >> ")

        if choice in MENU:
            coins = insert_money(choice)
            if coins == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += coins
                if check_ingredients(choice, resources):
                    make_coffee(choice, resources)
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif choice == "off":
            status = "OFF"
            print("Turned off")
            return 0
        else:
            print("please insert valid text")


main(starting_profit, starting_resources)
