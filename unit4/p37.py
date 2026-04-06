import matplotlib.pyplot as plt

profit = []
years = [1,2,3,4,5]

for i in range(5):
    p = int(input("Enter profit: "))
    profit.append(p)

plt.plot(years, profit, marker='o')
plt.title("Profit of 5 Years")
plt.xlabel("Year")
plt.ylabel("Profit")

plt.show()
