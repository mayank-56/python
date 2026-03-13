# Define a user-defined exception
class NegativeNumberError(Exception):
    """Exception raised when a negative number is entered."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    else:
        print("You entered:", number)

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)

except NegativeNumberError as e:
    print("User Defined Exception Caught:", e)

except ValueError:
    print("Invalid input! Please enter an integer.")

finally:
    print("Program execution completed.")
