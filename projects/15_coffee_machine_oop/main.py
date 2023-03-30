from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    print(f"Welcome to our coffee shop!")
    # building menu
    menu = Menu()
    # bulding options
    options = menu.get_items()[:-1]
    # calling on CoffeeMaker class to call their methods
    coffe_maker = CoffeeMaker()
    # calling on MoneyMachine class to call their methods
    money_machine = MoneyMachine()
    # cost of the drinks
    cost = {"latte": 2.5, "espresso": 1.5, "cappuccino": 3.0}
    # machine is on until user input "off"
    machine_on = True
    while machine_on:
        
        
        selection = input(f"which drink you would like to have? {options} : ").lower()

        # TODO 2 : turn off coffee machine by using "off" command
        if selection == 'off':
            print("Turning off the coffee machine. Goodbye!")
            machine_on = False
        # TODO 3 : generate a report by using 'report' command
        elif selection == 'report':
            coffe_maker.report()
        # TODO 6 : Output profit in $
        elif selection == 'profit':
            profit = money_machine.report()
        else:
            # handles user's input and return values
            drink = menu.find_drink(selection)
            if drink is None:
                print("Sorry that item is not available.")
            else:
                # TODO 4 : check if resources are sufficient
                if coffe_maker.is_resource_sufficient(drink):
                    # TODO 5 : process coins and validate transaction
                    if money_machine.make_payment(cost[selection]):
                        coffe_maker.make_coffee(drink)


main()
