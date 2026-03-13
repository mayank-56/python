# Program to copy contents of one text file to another

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    
    with open(source_file, 'r') as src:
        
        content = src.read()

    
    with open(destination_file, 'w') as dest:
        
        dest.write(content)

    print("File copied successfully!")

except FileNotFoundError:
    print("Error: Source file not found.")
except IOError:
    print("Error: Unable to read or write file.")
