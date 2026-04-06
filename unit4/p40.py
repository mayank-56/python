import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("students.xlsx")

# Count Male and Female students
gender_count = df['Gender'].value_counts()

print("Number of Male and Female Students:")
print(gender_count)

# Create bar graph
gender_count.plot(kind='bar')

plt.title("Male and Female Students")
plt.xlabel("Gender")
plt.ylabel("Number of Students")

plt.show()
