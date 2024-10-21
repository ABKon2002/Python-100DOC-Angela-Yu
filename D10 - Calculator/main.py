from art import logo

print(logo)
print("************CALCULATOR 1.0************")

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero! Try again."
    return n1 / n2

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    
    for symbol in operations_dict:
        print(symbol)
    
    continueFlag = True
    
    while continueFlag:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations_dict:
            print("Invalid operation symbol. Restart the program.")
            break
        
        num2 = float(input("Enter another number: "))
        
        calculation_function = operations_dict[operation_symbol]
        
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        continue_input = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ")
        if continue_input == 'n':
            calculator()
        continueFlag = continue_input == 'y'
    
calculator()
