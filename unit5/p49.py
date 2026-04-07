import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

# Input roll number to delete
roll = int(input("Enter Roll Number to delete: "))

# Delete query
sql = "DELETE FROM student WHERE rollno=%s"
val = (roll,)

cur.execute(sql, val)

# Save changes
con.commit()

# Check if record deleted
if cur.rowcount > 0:
    print("Record deleted successfully")
else:
    print("Student not found")

# Close connection
con.close()
