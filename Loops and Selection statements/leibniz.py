# Put your code here
num = int(input("Enter the number of iterations: "))
pi = 0

for i in range(num):
    pi = pi + 4 * (-1) ** i / (2* i + 1)

print("The approximation of pi is", pi)
    
