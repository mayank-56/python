import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

# Input roll number to search
roll = int(input("Enter Roll Number to search: "))

# Execute query
cur.execute("SELECT * FROM student WHERE rollno=%s", (roll,))

# Fetch record
row = cur.fetchone()

# Check if student exists
if row:
    print("Student Found")
    print("Roll No:", row[0])
    print("Name:", row[1])
    print("Gender:", row[2])
    print("Age:", row[3])
    print("Email:", row[4])
    print("Mobile:", row[5])
    print("City:", row[6])
else:
    print("Student not found")

# Close connection
con.close()
