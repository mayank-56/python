# Outer class
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.address = self.Address()  

    class Address:
        def __init__(self):
            self.city = "Unknown"
            self.state = "Unknown"
        
        def set_address(self, city, state):
            self.city = city
            self.state = state
        
        def get_address(self):
            return f"{self.city}, {self.state}"
    
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Address: {self.address.get_address()}")



student1 = Student("Alice", 101)

student1.address.set_address("New York", "NY")

student1.display()
