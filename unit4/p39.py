import matplotlib.pyplot as plt

ages = []

# Enter age of 50 students
for i in range(50):
    age = int(input("Enter age of student: "))
    ages.append(age)

# Define age groups (bins)
bins = [0,10,20,30,40,50,60,120]

# Create histogram
plt.hist(ages, bins=bins, edgecolor='black')

plt.title("Histogram of Student Ages")
plt.xlabel("Age Groups")
plt.ylabel("Number of Students")

plt.show()
    
