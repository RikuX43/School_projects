salary = int(input('Enter the starting salary: $'))
annual_Increase = (float(input('Enter the annual % increase: ')) / 100)
years = int(input('Enter the number of years: '))
print('Year\tSalary')
print('--------------')
for year in range(1, years + 1):
    print(year,'\t',format(salary, '.2f'))
    salary = salary + salary * annual_Increase
    
