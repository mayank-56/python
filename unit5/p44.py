import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

cur.execute("SELECT * FROM student")

row = cur.fetchone()

while row:
    print(row)
    row = cur.fetchone()

con.close()
