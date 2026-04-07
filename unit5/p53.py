import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

while True:
    print("\n----- STUDENT MENU -----")
    print("1. Insert Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. List Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Insert Student
    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        gender = input("Enter Gender: ")
        age = int(input("Enter Age: "))
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")
        city = input("Enter City: ")

        sql = "INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (roll, name, gender, age, email, mobile, city)
        cur.execute(sql, val)
        con.commit()
        print("Student inserted successfully")

    # Update Student
    elif choice == 2:
        roll = int(input("Enter Roll No to update: "))
        name = input("Enter New Name: ")
        city = input("Enter New City: ")

        sql = "UPDATE student SET name=%s, city=%s WHERE rollno=%s"
        val = (name, city, roll)
        cur.execute(sql, val)
        con.commit()

        if cur.rowcount > 0:
            print("Record updated successfully")
        else:
            print("Student not found")

    # Search Student
    elif choice == 3:
        roll = int(input("Enter Roll No to search: "))
        sql = "SELECT * FROM student WHERE rollno=%s"
        cur.execute(sql, (roll,))
        row = cur.fetchone()

        if row:
            print("Roll No:", row[0])
            print("Name:", row[1])
            print("Gender:", row[2])
            print("Age:", row[3])
            print("Email:", row[4])
            print("Mobile:", row[5])
            print("City:", row[6])
        else:
            print("Student not found")

    # Delete Student
    elif choice == 4:
        roll = int(input("Enter Roll No to delete: "))
        sql = "DELETE FROM student WHERE rollno=%s"
        cur.execute(sql, (roll,))
        con.commit()

        if cur.rowcount > 0:
            print("Record deleted successfully")
        else:
            print("Student not found")

    # List Students
    elif choice == 5:
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()

        print("\nStudent List:")
        for row in rows:
            print(row)

    # Exit
    elif choice == 6:
        print("Program exited")
        break

    else:
        print("Invalid choice")

con.close()
