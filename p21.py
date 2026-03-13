# Program to read student marks from file and calculate total, percentage and grade

filename = input("Enter the file name: ")

try:
    with open(filename, 'r') as file:
        print("\nStudent Details:\n")
        print("RollNo  Name     Total  Percentage  Grade")
        print("-------------------------------------------")

        for line in file:
            data = line.strip().split(',')

            rollno = data[0]
            name = data[1]
            marks = list(map(int, data[2:6]))

            total = sum(marks)
            percentage = total / 4

            # Grade calculation
            if percentage >= 90:
                grade = 'A'
            elif percentage >= 75:
                grade = 'B'
            elif percentage >= 60:
                grade = 'C'
            elif percentage >= 50:
                grade = 'D'
            else:
                grade = 'F'

            print(f"{rollno:<7} {name:<8} {total:<6} {percentage:<10.2f} {grade}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)
