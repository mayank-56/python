import matplotlib.pyplot as plt

courses = []
students = []

# Input for 5 courses
for i in range(5):
    c = input("Enter course name: ")
    s = int(input("Enter number of students: "))
    
    courses.append(c)
    students.append(s)

# Find course with maximum students
max_index = students.index(max(students))

# Create explode list (separate the largest slice)
explode = [0,0,0,0,0]
explode[max_index] = 0.2

# Create pie chart
plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%')

plt.title("Students in Different Courses")

plt.show()
