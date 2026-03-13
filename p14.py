# Write a program to display basic exception handling in python.
def divide_numbers():
    try:
    
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        result = numerator / denominator
        
    except ZeroDivisionError:
     
        print("Error: You cannot divide by zero!")
        
    except ValueError:
 
        print("Error: Please enter valid numeric values.")
        
    except Exception as e:
       
        print(f"An unexpected error occurred: {e}")
        
    else:
       
        print(f"Success! The result is {result}")
        
    finally:
        
        print("Execution complete. Cleaning up resources...")

divide_numbers()
