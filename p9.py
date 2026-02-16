# Write a program to create a function which accepts 2 numbers and one arithmetic operator. Return the answer accordingly.
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Error: Invalid operator."

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %, **): ")

result = calculate(n1, n2, op)
print(f"Result: {result}")
