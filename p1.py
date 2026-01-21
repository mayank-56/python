# 1. Write a program to input p, r, n and find out interest using simple input output statement.

p = float(input("Enter principal (p): "))
r = float(input("Enter rate of interest (r): "))
n = float(input("Enter time (n): "))

si = (p * r * n) / 100

print("Simple Interest =", si)
