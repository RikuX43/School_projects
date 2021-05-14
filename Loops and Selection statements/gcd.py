# Put your code here
small = int(input("Enter the first number? "))
large = int(input("Enter the larger number?"))

remainder = small%large

while remainder:
    small = large 
    large = remainder
    remainder = small%large
print("The greates common divisor is", large)
