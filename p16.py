# Write a program to generate arithmetic exception and log the exception in system.
import logging

# Configure logging
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,        
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result is:", result)

except ZeroDivisionError as e:
    print("Arithmetic Exception Occurred! Cannot divide by zero.")
    logging.error("Arithmetic Exception: %s", e)

except ValueError as e:
    print("Invalid input! Please enter integers only.")
    logging.error("Value Error: %s", e)

finally:
    print("Program execution completed.")
