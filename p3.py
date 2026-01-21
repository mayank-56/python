# 3. Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))

total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "Fail"

print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
