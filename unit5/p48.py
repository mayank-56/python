import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

# Input roll number of student to update
roll = int(input("Enter Roll Number to update: "))

# New details
name = input("Enter New Name: ")
gender = input("Enter New Gender: ")
age = int(input("Enter New Age: "))
email = input("Enter New Email: ")
mobile = input("Enter New Mobile: ")
city = input("Enter New City: ")

# Update query
sql = """UPDATE student 
         SET name=%s, gender=%s, age=%s, email=%s, mobile=%s, city=%s 
         WHERE rollno=%s"""

val = (name, gender, age, email, mobile, city, roll)

cur.execute(sql, val)

# Save changes
con.commit()

if cur.rowcount > 0:
    print("Record updated successfully")
else:
    print("Student not found")

# Close connection
con.close()
