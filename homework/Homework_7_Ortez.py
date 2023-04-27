storeSales = [0]*7
totalSales = 0

for i in range(7):
    storeSales[i] = int(input('Enter sales for day:', ))
    totalSales += storeSales[i]

print("Your daily sales were:", storeSales)
print("The total sales for the week are:", totalSales)
