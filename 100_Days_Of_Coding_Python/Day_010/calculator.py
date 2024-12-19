from replit import clear
from art import logo

print(logo)

def calculator(num1, op, num2):
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        return
    return result

keep_going = ""
while (keep_going in ["", "y", "n"]):
    
    if keep_going in ["", "n"]:
        first_number = float(input("What's the first number?: "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        
    elif keep_going == "y":
        print(f"The last result was {first_number}.")
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
    
    result = calculator(first_number, operation, second_number)
        
    if result == None:
        print("Wrong operator.")
        keep_going = "n"
    else:
        print(f"{first_number} {operation} {second_number} = {result}")
        keep_going = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'stop' to stop using the calculator: ")
    
    if keep_going == "y":
        first_number = result
    
    if keep_going == "stop":\
        clear()
    else:
        clear()
        print(logo)