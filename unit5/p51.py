import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

# Execute query to get all records
cur.execute("SELECT * FROM student")

rows = cur.fetchall()

print("Students whose name starts with 'N' and length is 5:\n")

for row in rows:
    name = row[1]
    
    if name.startswith('N') and len(name) == 5:
        print("Roll No:", row[0])
        print("Name:", row[1])
        print("Gender:", row[2])
        print("Age:", row[3])
        print("Email:", row[4])
        print("Mobile:", row[5])
        print("City:", row[6])
        print("---------------------")

# Close connection
con.close()
