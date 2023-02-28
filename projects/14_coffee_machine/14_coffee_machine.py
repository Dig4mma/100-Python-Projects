from menu_resources import MENU, resources, coins


# a function to report remaining ingredients and the amount of money earned
def report(money):
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")


# a function to handle resources, keeps track of whats running out
def resource_management(product):
    requiered_resource = MENU[product]['ingredients']
    for items in requiered_resource:
        if resources[items] < requiered_resource[items]:
            print(f"Sorry, there is not enough {items}.")
            return False
        else:
            resources[items] -= requiered_resource[items]
    return True


# a function to handle prices and inserted coins
def coin_processing(product):
    print("Please insert coins.")
    quarters = float(input(f"how many quarters?: ")) * coins['quarters']
    dimes = float(input(f"how many dimes?: ")) * coins['dimes']
    nickles = float(input(f"how many nickles?: ")) * coins['nickles']
    pennies = float(input(f"how many pennies?: ")) * coins['pennies']
    inserted_coins = quarters + dimes + nickles + pennies
    if inserted_coins < MENU[product]['cost']:
        print("Sorry, that's not enough money. Money Refunded.")
        return False
    else:
        change = round(inserted_coins - MENU[product]['cost'], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {product} ☕️. Enjoy!")
        return True


profit = 0
machine_is_on = True
while machine_is_on:
    # commands
    user_input = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    commands = ['off', 'report', 'espresso', 'latte', 'coppucino']
    # if off
    if user_input == 'off':
        machine_is_on = False
        break
    # report
    elif user_input == 'report':
        report(profit)
    # products
    else:
        # resource check
        resource = resource_management(user_input)
        # resources are insufficient
        if not resource:
            pass
        # resources are enough
        else:
            # money is enough
            coin = coin_processing(user_input)
            if not coin:
                break
            else:
                profit += MENU[user_input]['cost']


