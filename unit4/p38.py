import matplotlib.pyplot as plt

companies = []
employees = []

# Input for 5 companies
for i in range(5):
    name = input("Enter company name: ")
    emp = int(input("Enter number of employees: "))
    
    companies.append(name)
    employees.append(emp)

# Bar graph
plt.bar(companies, employees)

plt.title("Company Employee Size")
plt.xlabel("Company Name")
plt.ylabel("Number of Employees")

plt.show()
