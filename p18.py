def process_file(file_name):
    try:
       
        with open(file_name, 'r') as file:
          
            content = file.read()
            
            print("--- File Contents ---")
            print(content)
            print("----------------------")
            
            words = content.split()
            word_count = len(words)
            
            print(f"Total number of words: {word_count}")
            
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

process_file('data.txt')
