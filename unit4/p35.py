import pandas as pd

# Load Excel file
df = pd.read_excel("students.xlsx")

# 1) List of students from Rajkot City
print("Students from Rajkot City:")
rajkot_students = df[df['City'] == 'Rajkot']
print(rajkot_students)

print("\n")

# 2) List of Male students
print("Male Students:")
male_students = df[df['Gender'] == 'Male']
print(male_students)

print("\n")

# 3) List of Male students from Rajkot City
print("Male Students from Rajkot City:")
male_rajkot = df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')]
print(male_rajkot)

print("\n")

# 4) List of students whose age >= 20
print("Students with Age >= 20:")
age_students = df[df['Age'] >= 20]
print(age_students)
