### Calculator
from art import logo

def add(n1, n2):
    """Addition"""
    return n1 + n2
def subtract(n1, n2):
    """Subtraction"""
    return n1 - n2
def multiply(n1, n2):
    """Multiply"""
    return n1 * n2
def divide(n1, n2):
    """divide"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))

    for symble in operations:
        print(symble)

    should_continue = True

    while should_continue:
        operation_symble = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        calculate = operations[operation_symble]
        answer = calculate(num1, num2)
        print(f" {num1} {operation_symble} {num2} = {answer}")

        flag = input(f"Do you want to continue calculation with {answer}? y for yes or f for fresh calculation or anything for exit: ")
        if flag == 'y':
            num1 = answer
        elif flag == "f":
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()