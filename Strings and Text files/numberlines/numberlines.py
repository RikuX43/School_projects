inputFileName = input("Input filename: ") 
outputFileName = input("Output filename: ") 

inputFile = open(inputFileName, "r") 
outputFile = open(outputFileName, "w") 
count = 1 

for line in inputFile: 
    newLine = str(count).rjust(4, " ") + "> " + line 
    outputFile.write(newLine) 
    print(newLine) 
    count += 1  
