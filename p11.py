# Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.
def total_sum(*args):
    """
    Accepts any number of numeric arguments and returns their sum.
    """
    result = sum(args)
    return result

print("Total (10, 20):", total_sum(10, 20))
print("Total (1, 2, 3, 4, 5):", total_sum(1, 2, 3, 4, 5))
print("Total (100):", total_sum(100))
