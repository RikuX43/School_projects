# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:07:50 2021

@author: Riku
"""
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