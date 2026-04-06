class Father:
    def skill(self):
        print("Father: Gardening")

class Mother:
    def skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill(self):
        super().skill()
        print("Child: Gaming")

# Displaying the MRO
print("MRO for Child class:")
for cls in Child.mro():
    print(cls.__name__)

print("\nExecuting skill():")
c = Child()
c.skill()
