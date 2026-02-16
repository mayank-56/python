# Write a Python program to perform following operation on given string input:
# a) Count Number of Vowel in given string
# b) Count Length of string (donot use len() )
# c) Reverse string
# d) Find and replace operation
# e) check whether string entered is a palindrome or not
def string_manipulator():
    text = input("Enter a string: ")
    
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in text if char in vowels)
    
    length = 0
    for _ in text:
        length += 1

        reversed_text = text[::-1]
    
    find_val = input("Enter character/word to find: ")
    replace_val = input("Enter replacement: ")
    modified_text = text.replace(find_val, replace_val)
    
    is_palindrome = text.lower() == reversed_text.lower()

    print("\n--- Results ---")
    print(f"Vowel Count: {v_count}")
    print(f"String Length: {length}")
    print(f"Reversed String: {reversed_text}")
    print(f"Modified String: {modified_text}")
    print(f"Is Palindrome? {'Yes' if is_palindrome else 'No'}")

string_manipulator()
