import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

# Taking input from user
roll = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
gender = input("Enter Gender: ")
age = int(input("Enter Age: "))
email = input("Enter Email: ")
mobile = input("Enter Mobile: ")
city = input("Enter City: ")

# SQL query to insert data
sql = "INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s)"
val = (roll, name, gender, age, email, mobile, city)

cur.execute(sql, val)

# Save changes
con.commit()

print("Record inserted successfully")

# Close connection
con.close()
