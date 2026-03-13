# Simple Student Management Program

file_name = "students.txt"

def add():
    with open(file_name, "a") as f:
        roll = input("Roll No: ")
        name = input("Name: ")
        f.write(roll + "," + name + "\n")
    print("Student Added\n")

def search():
    roll = input("Enter Roll No to search: ")
    with open(file_name, "r") as f:
        for line in f:
            if line.split(",")[0] == roll:
                print("Found:", line)
                return
    print("Student Not Found\n")

def display():
    with open(file_name, "r") as f:
        print("All Students:")
        print(f.read())

def update():
    roll = input("Enter Roll No to update: ")
    lines = open(file_name).readlines()
    with open(file_name, "w") as f:
        for line in lines:
            if line.split(",")[0] == roll:
                name = input("Enter New Name: ")
                f.write(roll + "," + name + "\n")
                print("Updated\n")
            else:
                f.write(line)

def delete():
    roll = input("Enter Roll No to delete: ")
    lines = open(file_name).readlines()
    with open(file_name, "w") as f:
        for line in lines:
            if line.split(",")[0] != roll:
                f.write(line)
    print("Deleted (if existed)\n")

while True:
    print("a) Add  b) Search  c) Display  d) Update  e) Delete  f) Exit")
    ch = input("Choice: ").lower()

    if ch == 'a': add()
    elif ch == 'b': search()
    elif ch == 'c': display()
    elif ch == 'd': update()
    elif ch == 'e': delete()
    elif ch == 'f': break
    else: print("Invalid Choice\n")
