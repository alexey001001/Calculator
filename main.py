def calc(operand1, operand2, operator):
    if operator == '+':
        return f'{operand1} + {operand2} = {operand1 + operand2}'
    elif operator == '-':
        return f'{operand1} - {operand2} = {operand1 - operand2}'
    elif operator == '/':
        try:
            return f'{operand1} / {operand2} = {operand1 / operand2}'
        except ZeroDivisionError:
            return "Division by zero!"

def getResult():
    while True:
        try:
            operand1 = int(input("The first operand? [int]"))
            break
        except ValueError:
            print('Need to enter a int number!')

    while True:
        try:
            operand2 = int(input("The second operand? [int]"))
            break
        except ValueError:
            print("Need to enter a int number!")

    while True:
        operator = input("Operator? ['+', '-' or '/']")
        if (operator not in ['+', '-', '/']):
            print("Enter '+', '-' or '/'")
        else:
            break
    return calc(operand1, operand2, operator)

def init():
    while True:
        print(getResult())
        while True:
            i = input("Continue calculations? ['y'/'n']")
            if i in ['y', 'n']:
                break
        if i == ("y" or "yes"):
            continue
        elif i == "n":
            print("Goodbye!")
            break

init()
