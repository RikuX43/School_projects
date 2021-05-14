# Edit the code below

theSum = 0.0
count = 1.0
data = input("Enter a number or press Enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    average = theSum / count
    count += 1   
    data = input("Enter the next number or Enter to quit: ")
print("The sum is", theSum)
print("The average is", average)
