# Write a program to create a list and perform various operations on list using menu.
def list_operations():
    my_list = []
    
    while True:
        print("\n--- LIST OPERATIONS MENU ---")
        print("1. Add element")
        print("2. Remove element")
        print("3. Display list")
        print("4. Check length")
        print("5. Sort list")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            my_list.append(item)
            print(f"'{item}' added successfully.")
            
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"'{item}' removed.")
            else:
                print("Error: Item not found in list.")
                
        elif choice == '3':
            print("Current List:", my_list)
            
        elif choice == '4':
            print(f"The list has {len(my_list)} elements.")
            
        elif choice == '5':
            my_list.sort()
            print("List sorted alphabetically/numerically.")
            
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice, please try again.")

list_operations()
