# Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = list(map(lambda x: x * 2, numbers))

evens = list(filter(lambda x: x % 2 == 0, numbers))

product = reduce(lambda x, y: x * y, numbers)

print(f"Original List: {numbers}")
print(f"Mapped (Doubled): {doubled}")
print(f"Filtered (Evens): {evens}")
print(f"Reduced (Total Product): {product}")
