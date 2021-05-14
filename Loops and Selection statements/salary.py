# Put your code here
import math
salary = int(input("Enter the starting salary: "))
annual = (float(input("Enter the annual % increase: ")) / 100)
years = int(input("Enter the number of years: "))

print(' {:<10s} {:<10s}' .format('Year', 'Salary'))
print('------------')
for i in range(1, years + 1):
    print('{:<10d} {:<10.2f}'.format(i, salary))
    salary = salary + salary * annual

    

