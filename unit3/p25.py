# Define the Student class
class Student:
    def __init__(self):
        self.RollNo = None
        self.Name = None
        self.Age = None
        self.Gender = None
    
    
    def AddStudent(self, rollno, name, age, gender):
        self.RollNo = rollno
        self.Name = name
        self.Age = age
        self.Gender = gender
    
    
    def DisplayStudent(self):
        print("Student Details:")
        print("Roll No:", self.RollNo)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Gender:", self.Gender)



student1 = Student()


student1.AddStudent(101, "Alice", 20, "Female")


student1.DisplayStudent()
