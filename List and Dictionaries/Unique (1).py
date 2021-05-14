filename = open(input("Enter the input file name: "))
myList =[]
for line in filename:
    myList.extend(line.split(" "))
myList.sort()
print(myList)
