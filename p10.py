# Write a program to create 4 lambda functions which shall accept 2 numbers and one arithmetic operator. As per arithmetic operator related lambda functions shall be invoked.
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

def execute_lambda():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op in operations:
            result = operations[op](num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid operator!")
            
    except ValueError:
        print("Invalid input! Please enter numeric values.")

execute_lambda()
