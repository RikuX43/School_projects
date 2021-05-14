# Put your code here
import math
num_organ = int(input("Enter the initial number of organisms: "))
rate_grow = int(input("Enter the rate of growth [a real number > 1]: "))
hour_rate = int(input("Enter the number of hours to achieve the rate of growth: "))
total_hours = int(input("Enter the total hours of growth: "))

growth = num_organ
count = total_hours//hour_rate

for i in range(count):
    growth = growth * rate_grow

print("The total population is ", growth)

