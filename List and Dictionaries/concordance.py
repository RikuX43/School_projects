# Put your code here
f=input('Enter the input file name: ')
inputFile = open(f,"r")
list={}
for word in inputFile.read().split():
    if word not in list:
        list[word] = 1
    else:
            list[word] += 1
            inputFile.close();
for i in sorted(list):
    print("{0} {1} ".format(i, list[i]));
