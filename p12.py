# Write a program to display the use of local, global and nonlocal variables
counter = 0

def outer_function():
  
    message = "Hello from Outer"
    
    def inner_function():

        global counter
        
    
        nonlocal message
        

        local_val = "I am local"
        
        counter += 1
        message = "Modified by Inner"
        
        print("--- Inside Inner Function ---")
        print("Local Variable:", local_val)
        print("Updated Nonlocal Message:", message)
        print("Updated Global Counter:", counter)

    inner_function()
    print("\n--- Back in Outer Function ---")
    print("Nonlocal Message is now:", message)

print("Initial Global Counter:", counter)
outer_function()
print("\n--- Final Global Scope ---")
print("Global Counter is now:", counter)
