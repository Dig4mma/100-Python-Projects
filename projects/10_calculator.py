# Calculator


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}


def calculator():

    calc = True
    num1 = float(input("Whats the first Number? "))
    while calc:
        for operation in operations:
            print(operation)
        operation_symbol = input("pick an operation from the operation symbol above: ")
        num2 = float(input("Whats the second Number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        decide = input(f"Type 'y' to continue calculating with {answer}, or press 'r' to reset. otherwise press any "
                       f"other key to quit : ").lower()

        if decide == 'y':
            num1 = answer
        elif decide == 'r':
            calculator()
        else:
            calc = False
            print("Bye!")


calculator()
