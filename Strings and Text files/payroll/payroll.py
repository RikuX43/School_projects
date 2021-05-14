# Put your code here
fileName = input("Enter the file name: ")

inputFile = open(fileName, 'r')
 
 # Read the data and print the report
print("%-15s%6s%15s" % ("Name", "Hours", "Total Pay"))
for line in inputFile:
        dataList = line.split()
        name = dataList[0]
        hours = int(dataList[1])
        payRate = float(dataList[2])
        totalPay = hours * payRate
        print("%-15s%6d%15.2f" % (name, hours, totalPay))
