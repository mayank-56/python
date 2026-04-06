class MyClass:
    # Class variable
    count = 0
    
    # Constructor / instance initialization
    def __init__(self, name):
        self.name = name  # instance variable
        MyClass.count += 1
    
    def greet(self):
        print(f"Hello, my name is {self.name}")
    
    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

obj1 = MyClass("Alice")
obj2 = MyClass("Bob")

obj1.greet()  
obj2.greet()  

MyClass.show_count()  
