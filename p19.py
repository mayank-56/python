def analyze_numbers(file_name):
    try:
        with open(file_name, 'r') as file:

            raw_data = file.read().split()
            
            numbers = [float(num) for num in raw_data]

            if not numbers:
                print("The file is empty.")
                return

            total_sum = sum(numbers)
            max_num = max(numbers)
            min_num = min(numbers)

            print(f"--- Statistics for {file_name} ---")
            print(f"Numbers found: {len(numbers)}")
            print(f"Total Sum:    {total_sum}")
            print(f"Maximum:      {max_num}")
            print(f"Minimum:      {min_num}")
            print("-" * 30)

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric characters.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

analyze_numbers('numbers.txt')
