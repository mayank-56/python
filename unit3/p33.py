class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __sub__(self, other):
        return self.val - other.val

n1 = Number(20)
n2 = Number(10)

print(f"Addition (20 + 10): {n1 + n2}")       
print(f"Subtraction (20 - 10): {n1 - n2}")    
