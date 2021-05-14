# Put your code here
wage = float(input('Enter the wage: '))
reg_hours = int(input('Enter the regular hours: '))
ot_hours = int(input('Enter the overtime hours: '))

weekly_pay = wage * reg_hours + ot_hours * wage * 1.5

print("The total weekly pay is $", weekly_pay)
