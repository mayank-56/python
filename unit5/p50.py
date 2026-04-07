import mysql.connector
import re

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

# Execute query
cur.execute("SELECT * FROM student")

rows = cur.fetchall()

# Regular expression for valid email
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

print("Students with Valid Email:\n")

for row in rows:
    email = row[4]
    
    if re.match(pattern, email):
        print("Roll No:", row[0])
        print("Name:", row[1])
        print("Gender:", row[2])
        print("Age:", row[3])
        print("Email:", row[4])
        print("Mobile:", row[5])
        print("City:", row[6])
        print("----------------------")

con.close()
