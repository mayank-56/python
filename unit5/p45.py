import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

# Create cursor object
cur = con.cursor()

# Execute query
cur.execute("SELECT * FROM student")

# Fetch all records
rows = cur.fetchall()

# Display records
for row in rows:
    print("Roll No:", row[0])
    print("Name:", row[1])
    print("Gender:", row[2])
    print("Age:", row[3])
    print("Email:", row[4])
    print("Mobile:", row[5])
    print("City:", row[6])
    print("----------------------")

# Close connection
con.close()
