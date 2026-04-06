# Base class
class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

# Derived class
class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee
    
    def display(self):
        print(f"RollNo: {self.rollno}, Name: {self.name}, Gender: {self.gender}, Age: {self.age}")
        print(f"Course: {self.coursename}, Duration: {self.duration}, Fee: {self.fee}")

c = Course(101, "Alice", "Female", 20, "Python", "3 months", 1500)
c.display()
